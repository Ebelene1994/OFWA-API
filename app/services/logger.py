from sqlalchemy.orm import Session
from app.models.analysis import AnalysisLog

def save_analysis_log(
    db: Session,
    filename: str,
    results: dict
) -> AnalysisLog:
    record = AnalysisLog(
        filename=filename,
        total_sites=results["total_sites"],
        top_region=results["top_region"],
        average_sites_per_region=results["average_sites_per_region"],
        cities_above_threshold=results["cities_above_threshold"]
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return record
