import pytest
from sqlalchemy.orm import Session
from app.database import Base, engine, SessionLocal
from app.services.logger import save_analysis_log

from app.models.analysis import AnalysisLog

@pytest.fixture(scope="module")
def db_session():
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

def test_save_analysis(db_session: Session):
    results = {
        "total_sites": 20,
        "top_region": "R1",
        "average_sites_per_region": 10.0,
        "cities_above_threshold": ["A"]
    }
    log = save_analysis_log(db_session, "test.xlsx", results)
    assert log.id is not None
    assert log.filename == "test.xlsx"
