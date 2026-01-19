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

def test_save_analysis(db_session: Session):
    results = {
        "total_sites": 20,
        "top_region": "R1",
        "average_sites_per_region": 10.0,
        "cities_above_threshold": ["A"]
    }
    csv_text = "city,region,sites\nA,R1,10\nB,R2,10\n"
    log = save_analysis_log(db_session, "test.csv", results, csv_text)
    assert log.id is not None
    assert log.filename == "test.csv"
    assert isinstance(log.csv_text, str)
    assert "city,region,sites" in log.csv_text
