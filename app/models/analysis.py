from sqlalchemy import Column, Integer, String, Float, DateTime, JSON
from datetime import datetime
from app.database import Base

class AnalysisLog(Base):
    __tablename__ = "analysis_logs"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    total_sites = Column(Integer, nullable=False)
    top_region = Column(String, nullable=False)
    average_sites_per_region = Column(Float, nullable=False)
    cities_above_threshold = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
