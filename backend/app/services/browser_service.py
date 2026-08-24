import os
import subprocess
import json
from typing import List, Optional
from app.schemas import BrowserStatus, ChromeProfile
from app.services.log_service import LogService

class BrowserService:
    _active_profile = "Default"
    
    @classmethod
    def get_chrome_path(cls) -> Optional[str]:
        # Search common Windows locations
        paths = [
            os.path.expandvars(r"%PROGRAMFILES%\Google\Chrome\Application\chrome.exe"),
            os.path.expandvars(r"%PROGRAMFILES(X86)%\Google\Chrome\Application\chrome.exe"),
            os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe")
        ]
        for path in paths:
            if os.path.exists(path):
                return path
        return None

    @classmethod
    def get_status(cls) -> BrowserStatus:
        path = cls.get_chrome_path()
        return BrowserStatus(
            available=path is not None,
            browser="Google Chrome",
            active_profile=cls._active_profile
        )

    @classmethod
    def get_profiles(cls) -> List[ChromeProfile]:
        # In a real app, parse %LOCALAPPDATA%\Google\Chrome\User Data\Local State
        # For this MVP, we will return a minimal list, and simulate finding standard directories
        user_data_path = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data")
        profiles = []
        if os.path.exists(user_data_path):
            # Check for Default and Profile X dirs
            for item in os.listdir(user_data_path):
                if item == "Default" or item.startswith("Profile "):
                    if os.path.isdir(os.path.join(user_data_path, item)):
                        profiles.append(ChromeProfile(name=item, display_name=item))
        
        if not profiles:
            # Fallback if Chrome doesn't exist or no data folder
            profiles = [
                ChromeProfile(name="Default", display_name="Default"),
                ChromeProfile(name="Profile 1", display_name="Secondary Profile")
            ]
        return profiles

    @classmethod
    def set_profile(cls, profile_name: str) -> bool:
        cls._active_profile = profile_name
        LogService.add_log("INFO", f"Active Chrome profile set to: {profile_name}")
        return True

    @classmethod
    def open_url(cls, url: str) -> bool:
        if not (url.startswith("http://") or url.startswith("https://")):
            LogService.add_log("ERROR", f"Invalid URL requested: {url}")
            return False
            
        chrome_path = cls.get_chrome_path()
        if not chrome_path:
            LogService.add_log("ERROR", "Chrome executable not found.")
            return False
            
        try:
            cmd = [chrome_path, f'--profile-directory={cls._active_profile}', url]
            subprocess.Popen(cmd)
            LogService.add_log("INFO", f"Opened URL {url} in profile {cls._active_profile}")
            return True
        except Exception as e:
            LogService.add_log("ERROR", f"Failed to open URL: {e}")
            return False

    @classmethod
    def open_youtube(cls) -> bool:
        return cls.open_url("https://www.youtube.com")
