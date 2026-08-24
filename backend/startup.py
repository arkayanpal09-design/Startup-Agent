import sys
import os
import time

# Ensure backend root is in PYTHONPATH
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.startup_service import StartupService
from app.services.network_service import NetworkService
from app.services.browser_service import BrowserService
from app.services.log_service import LogService

def main():
    LogService.add_log("INFO", "NOVA startup agent started")
    
    config = StartupService.get_config()
    LogService.add_log("INFO", "Configuration loaded")
    
    if not config.startup_enabled:
        LogService.add_log("INFO", "Startup automation is disabled. Exiting.")
        return

    LogService.add_log("INFO", f"Waiting {config.startup_delay_seconds} seconds")
    time.sleep(config.startup_delay_seconds)
    
    if config.wait_for_network:
        LogService.add_log("INFO", "Checking network")
        timeout_reached = True
        for _ in range(0, config.network_timeout_seconds, config.network_retry_interval_seconds):
            net_status = NetworkService.check_connection()
            if net_status.connected:
                LogService.add_log("INFO", "Internet connection available")
                timeout_reached = False
                break
            time.sleep(config.network_retry_interval_seconds)
            
        if timeout_reached:
            LogService.add_log("ERROR", "Network connection timeout reached")
            return
    
    BrowserService._active_profile = config.chrome_profile
    chrome_path = BrowserService.get_chrome_path()
    if not chrome_path:
        LogService.add_log("ERROR", "Chrome executable not found")
        return
    else:
        LogService.add_log("INFO", "Chrome detected")
    
    profiles = BrowserService.get_profiles()
    profile_names = [p.name for p in profiles]
    if config.chrome_profile not in profile_names:
        LogService.add_log("ERROR", "Configured Chrome profile not found")
        return
        
    LogService.add_log("INFO", f"Chrome profile: {config.chrome_profile}")
    
    # Launch URLs securely
    for url in config.startup_urls:
        if not (url.startswith("http://") or url.startswith("https://")):
            LogService.add_log("WARNING", f"Ignoring non-HTTP URL: {url}")
            continue
            
        if "youtube.com" in url:
            LogService.add_log("INFO", "Opening YouTube")
        
        BrowserService.open_url(url)
        time.sleep(1) # wait slightly between spawning tabs
        
    LogService.add_log("INFO", "Startup workflow completed")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        LogService.add_log("ERROR", f"Startup workflow failed: {e}")
