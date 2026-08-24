import datetime
from app.schemas import LogEntry
from typing import List, Optional

class LogService:
    _logs: List[LogEntry] = []

    @classmethod
    def add_log(cls, level: str, message: str) -> None:
        entry = LogEntry(
            timestamp=datetime.datetime.utcnow().isoformat() + "Z",
            level=level,
            message=message
        )
        cls._logs.insert(0, entry) # Insert at beginning
        # Keep only the last 1000 logs in memory for this MVP
        if len(cls._logs) > 1000:
            cls._logs = cls._logs[:1000]

    @classmethod
    def get_logs(cls, limit: int = 100, level: Optional[str] = None, search: Optional[str] = None) -> List[LogEntry]:
        filtered = cls._logs
        if level:
            filtered = [log for log in filtered if log.level.upper() == level.upper()]
        if search:
            s = search.lower()
            filtered = [log for log in filtered if s in log.message.lower()]
            
        return filtered[:limit]
