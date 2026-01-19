from pydantic import BaseModel, ConfigDict
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

    model_config = ConfigDict(from_attributes=True)
