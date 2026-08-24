import datetime
from app.schemas import AgentStatus
from app.services.browser_service import BrowserService
from app.services.network_service import NetworkService
from app.services.startup_service import StartupService
from app.services.log_service import LogService

class AgentService:
    _is_running = True
    _last_startup = "Never"

    @classmethod
    def get_status(cls) -> AgentStatus:
        net_status = NetworkService.check_connection(timeout=1.0)
        browser_status = BrowserService.get_status()
        config = StartupService.get_config()

        return AgentStatus(
            running=cls._is_running,
            status="online" if cls._is_running else "stopped",
            startup_automation_enabled=config.startup_enabled,
            internet_connected=net_status.connected,
            chrome_available=browser_status.available,
            active_chrome_profile=browser_status.active_profile,
            last_startup=cls._last_startup
        )

    @classmethod
    def start_agent(cls):
        cls._is_running = True
        cls._last_startup = datetime.datetime.utcnow().isoformat() + "Z"
        LogService.add_log("INFO", "Agent started.")
        return {"success": True, "message": "Agent started"}

    @classmethod
    def stop_agent(cls):
        cls._is_running = False
        LogService.add_log("WARNING", "Agent stopped.")
        return {"success": True, "message": "Agent stopped"}

    @classmethod
    def restart_agent(cls):
        cls.stop_agent()
        cls.start_agent()
        LogService.add_log("INFO", "Agent restarted.")
        return {"success": True, "message": "Agent restarted"}
