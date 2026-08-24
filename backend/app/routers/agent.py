from fastapi import APIRouter
from app.services.agent_service import AgentService
from app.schemas import AgentStatus, SuccessResponse

router = APIRouter(prefix="/agent", tags=["Agent"])

@router.get("/status", response_model=AgentStatus)
def get_agent_status():
    return AgentService.get_status()

@router.post("/start", response_model=SuccessResponse)
def start_agent():
    return AgentService.start_agent()

@router.post("/stop", response_model=SuccessResponse)
def stop_agent():
    return AgentService.stop_agent()

@router.post("/restart", response_model=SuccessResponse)
def restart_agent():
    return AgentService.restart_agent()
