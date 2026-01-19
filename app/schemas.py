from pydantic import BaseModel
from typing import List
from datetime import datetime

class AnalysisResponse(BaseModel):
    id: int
    filename: str
    total_sites: int
    top_region: str
    average_sites_per_region: float
    cities_above_threshold: List[str]
    created_at: datetime

    class Config:
        orm_mode = True
