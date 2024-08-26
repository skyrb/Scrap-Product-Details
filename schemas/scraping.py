from pydantic import BaseModel
from typing import List, Optional

class ScrapeRequest(BaseModel):
    num_pages: int
    proxy: Optional[str] = None  # Proxy string is optional

class ScrapeResponse(BaseModel):
    data: List[dict]

