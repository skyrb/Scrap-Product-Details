from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from services.scraper_service import ScraperService
from storage.json_storage import JSONStorageService
from notifications.console_notification import ConsoleNotificationService
from schemas.scraping import ScrapeRequest, ScrapeResponse
from config.config import Config

# Router initialization
router = APIRouter()

# Authentication dependency
security = HTTPBearer()


def authenticate(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != Config.STATIC_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

# Define a route to scrape data
@router.post("/scrape", response_model=ScrapeResponse, dependencies=[Depends(authenticate)])
async def scrape(scrape_request: ScrapeRequest):
    # Create instances of the storage and notification services
    storage_service = JSONStorageService()
    notification_service = ConsoleNotificationService()

    scraper_service = ScraperService(storage_service, notification_service)
    

    scraped_data = scraper_service.scrape(
        num_pages=scrape_request.num_pages,
        proxy=scrape_request.proxy
    )

    return ScrapeResponse(data=scraped_data)
