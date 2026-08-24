from fastapi import APIRouter, Query
from typing import Optional
from app.services.log_service import LogService
from app.schemas import LogsResponse

router = APIRouter(prefix="/logs", tags=["Logs"])

@router.get("", response_model=LogsResponse)
def get_logs(limit: int = 100, level: Optional[str] = None, search: Optional[str] = None):
    logs = LogService.get_logs(limit=limit, level=level, search=search)
    return {"logs": logs}
