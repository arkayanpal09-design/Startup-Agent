import json
import os
import time
from app.schemas import StartupConfig, StartupWorkflowResult, WorkflowStepResult
from app.services.browser_service import BrowserService
from app.services.network_service import NetworkService
from app.services.log_service import LogService

CONFIG_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), "config", "config.json")

class StartupService:
    @classmethod
    def get_config(cls) -> StartupConfig:
        default_config = StartupConfig()
        if not os.path.exists(CONFIG_FILE):
            return default_config
        try:
            with open(CONFIG_FILE, "r") as f:
                data = json.load(f)
                
            # Perform safe migration from older keys
            migrated_data = {}
            migrated_data["startup_enabled"] = data.get("startup_enabled", data.get("enabled", default_config.startup_enabled))
            migrated_data["startup_delay_seconds"] = data.get("startup_delay_seconds", data.get("startup_delay", default_config.startup_delay_seconds))
            migrated_data["wait_for_network"] = data.get("wait_for_network", default_config.wait_for_network)
            migrated_data["network_timeout_seconds"] = data.get("network_timeout_seconds", data.get("network_timeout", default_config.network_timeout_seconds))
            migrated_data["network_retry_interval_seconds"] = data.get("network_retry_interval_seconds", data.get("retry_interval", default_config.network_retry_interval_seconds))
            migrated_data["chrome_profile"] = data.get("chrome_profile", default_config.chrome_profile)
            migrated_data["startup_urls"] = data.get("startup_urls", data.get("startup_websites", default_config.startup_urls))
            
            # Re-save cleanly upgraded config implicitly
            cfg = StartupConfig(**migrated_data)
            cls.update_config(cfg)
            return cfg
        except Exception as e:
            LogService.add_log("ERROR", f"Failed to load config, returning defaults: {e}")
            return default_config

    @classmethod
    def update_config(cls, config: StartupConfig) -> bool:
        os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
        try:
            with open(CONFIG_FILE, "w") as f:
                json.dump(config.model_dump(), f, indent=4)
            LogService.add_log("INFO", "Startup configuration updated successfully.")
            return True
        except Exception as e:
            LogService.add_log("ERROR", f"Failed to save config: {e}")
            return False

    @classmethod
    def run_workflow(cls) -> StartupWorkflowResult:
        LogService.add_log("INFO", "Starting automated PC workflow.")
        steps = []
        config = cls.get_config()

        # Step 1: Network
        if config.wait_for_network:
            net_status = NetworkService.check_connection()
            if net_status.connected:
                steps.append(WorkflowStepResult(name="network", status="success"))
                LogService.add_log("INFO", "Network confirmed connected.")
            else:
                steps.append(WorkflowStepResult(name="network", status="failed"))
                LogService.add_log("WARNING", "Network not connected, proceeding anyway.")
        
        # Step 2: Chrome
        browser_status = BrowserService.get_status()
        if browser_status.available:
            steps.append(WorkflowStepResult(name="chrome", status="success"))
            LogService.add_log("INFO", "Chrome detected.")
        else:
            steps.append(WorkflowStepResult(name="chrome", status="failed"))
            LogService.add_log("ERROR", "Chrome not detected. Aborting workflow.")
            return StartupWorkflowResult(success=False, steps=steps)

        # Step 3: Open Websites
        for site in config.startup_websites:
            success = BrowserService.open_url(site)
            steps.append(WorkflowStepResult(name=f"open_{site}", status="success" if success else "failed"))

        LogService.add_log("INFO", "Workflow completed.")
        return StartupWorkflowResult(success=True, steps=steps)
