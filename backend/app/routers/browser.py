from fastapi import APIRouter
from app.services.browser_service import BrowserService
from app.schemas import BrowserStatus, ChromeProfilesResponse, ChromeProfileRequest, SuccessResponse, OpenUrlRequest

router = APIRouter(prefix="/browser", tags=["Browser"])

@router.get("/status", response_model=BrowserStatus)
def get_browser_status():
    return BrowserService.get_status()

@router.get("/profiles", response_model=ChromeProfilesResponse)
def get_chrome_profiles():
    return {"profiles": BrowserService.get_profiles()}

@router.put("/profile", response_model=SuccessResponse)
def set_chrome_profile(request: ChromeProfileRequest):
    # Verify profile exists
    profiles = [p.name for p in BrowserService.get_profiles()]
    if request.profile in profiles:
        BrowserService.set_profile(request.profile)
        return {"success": True, "message": f"Profile set to {request.profile}"}
    return {"success": False, "message": "Invalid profile"}

@router.post("/youtube", response_model=SuccessResponse)
def open_youtube():
    success = BrowserService.open_youtube()
    return {"success": success, "message": "YouTube opened" if success else "Failed to open YouTube"}

@router.post("/open", response_model=SuccessResponse)
def open_url(req: OpenUrlRequest):
    success = BrowserService.open_url(req.url)
    return {"success": success, "message": f"URL opened" if success else "Failed to open URL"}
