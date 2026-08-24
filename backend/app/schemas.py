from pydantic import BaseModel, HttpUrl, Field
from typing import List, Optional

class HealthResponse(BaseModel):
    status: str
    service: str

class AgentStatus(BaseModel):
    running: bool
    status: str
    startup_automation_enabled: bool
    internet_connected: bool
    chrome_available: bool
    active_chrome_profile: str
    last_startup: str

class SuccessResponse(BaseModel):
    success: bool
    message: str

class WorkflowStepResult(BaseModel):
    name: str
    status: str

class StartupWorkflowResult(BaseModel):
    success: bool
    steps: List[WorkflowStepResult]

class StartupConfig(BaseModel):
    startup_enabled: bool = True
    startup_delay_seconds: int = Field(default=5, ge=0)
    wait_for_network: bool = True
    network_timeout_seconds: int = Field(default=60, gt=0)
    network_retry_interval_seconds: int = Field(default=5, gt=0)
    chrome_profile: str = Field(default="Default", min_length=1)
    startup_urls: List[str] = [
        "https://www.youtube.com"
    ]

class BrowserStatus(BaseModel):
    available: bool
    browser: str
    active_profile: str

class ChromeProfile(BaseModel):
    name: str
    display_name: str

class ChromeProfilesResponse(BaseModel):
    profiles: List[ChromeProfile]

class ChromeProfileRequest(BaseModel):
    profile: str

class OpenUrlRequest(BaseModel):
    url: str

class NetworkStatus(BaseModel):
    connected: bool
    latency_ms: int

class Application(BaseModel):
    id: str
    name: str
    path: str
    allowed: bool

class LogEntry(BaseModel):
    timestamp: str
    level: str
    message: str

class LogsResponse(BaseModel):
    logs: List[LogEntry]
