from fastapi import APIRouter
from app.services.network_service import NetworkService
from app.schemas import NetworkStatus

router = APIRouter(prefix="/network", tags=["Network"])

@router.get("/status", response_model=NetworkStatus)
def get_network_status():
    return NetworkService.check_connection()
