from fastapi import APIRouter
from app.services.startup_service import StartupService
from app.schemas import StartupConfig, StartupWorkflowResult, SuccessResponse

router = APIRouter(prefix="/startup", tags=["Startup"])

@router.get("/config", response_model=StartupConfig)
def get_startup_config():
    return StartupService.get_config()

@router.put("/config", response_model=SuccessResponse)
def update_startup_config(config: StartupConfig):
    success = StartupService.update_config(config)
    if success:
        return {"success": True, "message": "Configuration updated"}
    return {"success": False, "message": "Failed to update configuration"}

@router.post("/run", response_model=StartupWorkflowResult)
def run_startup_workflow():
    return StartupService.run_workflow()
