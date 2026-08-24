import pytest
from startup import main
from app.services.startup_service import StartupService
from app.schemas import StartupConfig
from app.services.log_service import LogService
from app.services.network_service import NetworkService
from app.services.browser_service import BrowserService

@pytest.fixture
def base_config():
    return StartupConfig(
        startup_enabled=True,
        startup_delay_seconds=0,
        wait_for_network=True,
        network_timeout_seconds=5,
        network_retry_interval_seconds=1,
        chrome_profile="Default",
        startup_urls=["https://www.youtube.com"]
    )

def test_startup_disabled(mocker, base_config):
    base_config.startup_enabled = False
    mocker.patch.object(StartupService, 'get_config', return_value=base_config)
    mock_log = mocker.patch.object(LogService, 'add_log')
    mocker.patch('time.sleep') # Prevent actual sleep
    mock_net = mocker.patch.object(NetworkService, 'check_connection')
    
    main()
    
    mock_net.assert_not_called()
    mock_log.assert_any_call("INFO", "Startup automation is disabled. Exiting.")

def test_missing_chrome(mocker, base_config):
    mocker.patch.object(StartupService, 'get_config', return_value=base_config)
    mocker.patch('time.sleep')
    mocker.patch.object(NetworkService, 'check_connection', return_value=type('obj', (object,), {'connected': True})())
    
    mocker.patch.object(BrowserService, 'get_chrome_path', return_value=None)
    mock_log = mocker.patch.object(LogService, 'add_log')
    
    main()
    
    mock_log.assert_any_call("ERROR", "Chrome executable not found")

def test_invalid_profile(mocker, base_config):
    base_config.chrome_profile = "InvalidMissingProfile"
    mocker.patch.object(StartupService, 'get_config', return_value=base_config)
    mocker.patch('time.sleep')
    mocker.patch.object(NetworkService, 'check_connection', return_value=type('obj', (object,), {'connected': True})())
    mocker.patch.object(BrowserService, 'get_chrome_path', return_value="C:/chrome.exe")
    
    mocker.patch.object(BrowserService, 'get_profiles', return_value=[type('obj', (object,), {'name': 'Default'})()])
    mock_log = mocker.patch.object(LogService, 'add_log')
    
    main()
    
    mock_log.assert_any_call("ERROR", "Configured Chrome profile not found")

def test_network_unavailable(mocker, base_config):
    mocker.patch.object(StartupService, 'get_config', return_value=base_config)
    mocker.patch('time.sleep')
    mocker.patch.object(NetworkService, 'check_connection', return_value=type('obj', (object,), {'connected': False})())
    mock_log = mocker.patch.object(LogService, 'add_log')
    
    main()
    
    mock_log.assert_any_call("ERROR", "Network connection timeout reached")

def test_wait_for_network_false(mocker, base_config):
    base_config.wait_for_network = False
    mocker.patch.object(StartupService, 'get_config', return_value=base_config)
    mocker.patch('time.sleep')
    mock_net = mocker.patch.object(NetworkService, 'check_connection')
    mocker.patch.object(BrowserService, 'get_chrome_path', return_value="C:/chrome.exe")
    mocker.patch.object(BrowserService, 'get_profiles', return_value=[type('obj', (object,), {'name': 'Default'})()])
    mocker.patch.object(BrowserService, 'open_url', return_value=True)
    
    main()
    
    mock_net.assert_not_called()

def test_successful_workflow(mocker, base_config):
    mocker.patch.object(StartupService, 'get_config', return_value=base_config)
    mocker.patch('time.sleep')
    mocker.patch.object(NetworkService, 'check_connection', return_value=type('obj', (object,), {'connected': True})())
    mocker.patch.object(BrowserService, 'get_chrome_path', return_value="C:/chrome.exe")
    mocker.patch.object(BrowserService, 'get_profiles', return_value=[type('obj', (object,), {'name': 'Default'})()])
    mock_open = mocker.patch.object(BrowserService, 'open_url', return_value=True)
    mock_log = mocker.patch.object(LogService, 'add_log')
    
    main()
    
    mock_open.assert_called_with("https://www.youtube.com")
    mock_log.assert_any_call("INFO", "Startup workflow completed")
