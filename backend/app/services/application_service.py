from typing import List, Optional
from app.schemas import Application
from app.services.log_service import LogService
import os
import subprocess

class ApplicationService:
    # MVP static configured applications
    _allowed_apps = [
        Application(id="notepad", name="Notepad", path="notepad.exe", allowed=True),
        Application(id="calc", name="Calculator", path="calc.exe", allowed=True)
    ]

    @classmethod
    def get_applications(cls) -> List[Application]:
        return cls._allowed_apps

    @classmethod
    def launch_application(cls, app_id: str) -> bool:
        app = next((a for a in cls._allowed_apps if a.id == app_id), None)
        if not app or not app.allowed:
            LogService.add_log("ERROR", f"Launch denied or app not found for {app_id}")
            return False
            
        try:
            # We enforce shell=False and restricted static paths
            subprocess.Popen([app.path])
            LogService.add_log("INFO", f"Launched application: {app.name}")
            return True
        except Exception as e:
            LogService.add_log("ERROR", f"Failed to launch {app.name}: {e}")
            return False
