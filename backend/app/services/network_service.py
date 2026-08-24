import socket
import time
from app.schemas import NetworkStatus

class NetworkService:
    @staticmethod
    def check_connection(host="8.8.8.8", port=53, timeout=3.0) -> NetworkStatus:
        """
        Check if the machine has active internet connection by attempting
        a socket connection to Google's public DNS.
        """
        try:
            start_time = time.time()
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            latency = int((time.time() - start_time) * 1000)
            return NetworkStatus(connected=True, latency_ms=latency)
        except Exception:
            return NetworkStatus(connected=False, latency_ms=0)
