import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.browser_service import BrowserService
from app.services.network_service import NetworkService

client = TestClient(app)

def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "nova-backend"}

def test_agent_status(mocker):
    # Mock network connection
    mocker.patch.object(NetworkService, 'check_connection', return_value=type('obj', (object,), {'connected': True, 'latency_ms': 10})())
    mocker.patch.object(BrowserService, 'get_status', return_value=type('obj', (object,), {'available': True, 'browser': 'Google Chrome', 'active_profile': 'Default'})())
    
    response = client.get("/api/agent/status")
    assert response.status_code == 200
    data = response.json()
    assert data["running"] == True
    assert data["internet_connected"] == True
    assert data["chrome_available"] == True

def test_browser_profiles(mocker):
    mocker.patch.object(BrowserService, 'get_profiles', return_value=[
        type('obj', (object,), {'name': 'Default', 'display_name': 'Default'})(),
        type('obj', (object,), {'name': 'Profile 1', 'display_name': 'Profile 1'})()
    ])
    
    response = client.get("/api/browser/profiles")
    assert response.status_code == 200
    data = response.json()
    assert "profiles" in data
    assert len(data["profiles"]) == 2

def test_network_status(mocker):
    mocker.patch.object(NetworkService, 'check_connection', return_value=type('obj', (object,), {'connected': True, 'latency_ms': 15})())
    
    response = client.get("/api/network/status")
    assert response.status_code == 200
    assert response.json()["connected"] == True
    assert response.json()["latency_ms"] == 15
