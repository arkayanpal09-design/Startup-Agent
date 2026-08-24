from fastapi import APIRouter
from typing import List
from app.services.application_service import ApplicationService
from app.schemas import Application, SuccessResponse

router = APIRouter(prefix="/applications", tags=["Applications"])

@router.get("", response_model=List[Application])
def get_applications():
    return ApplicationService.get_applications()

@router.post("/{app_id}/launch", response_model=SuccessResponse)
def launch_application(app_id: str):
    success = ApplicationService.launch_application(app_id)
    if success:
        return {"success": True, "message": f"Launched app {app_id}"}
    return {"success": False, "message": f"Failed to launch app {app_id}"}
