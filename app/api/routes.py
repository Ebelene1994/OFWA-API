from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException, Response
from sqlalchemy.orm import Session
import os
import shutil

from app.database import SessionLocal
from app.services.file_loader import load_file
from app.services.normalizer import normalize_columns
from app.services.analysis import analyze_data
from app.services.logger import save_analysis_log
from app.models.analysis import AnalysisLog
from app.schemas import AnalysisResponse
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/analyze", response_model=AnalysisResponse)
def analyze_dataset(
    file: UploadFile = File(...),
    threshold: int = Form(10),
    db: Session = Depends(get_db)
):
    try:
        os.makedirs("uploads", exist_ok=True)
        file_path = f"uploads/{file.filename}"

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        df = load_file(file_path)
        df = normalize_columns(df)
        results = analyze_data(df, threshold)

        csv_text = df.to_csv(index=False)

        return save_analysis_log(db, file.filename, results, csv_text)

    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))

@router.get("/analyses", response_model=List[AnalysisResponse])
def get_all_analyses(db: Session = Depends(get_db)):
    return db.query(AnalysisLog).all()

@router.get("/analyses/{analysis_id}", response_model=AnalysisResponse)
def get_analysis(analysis_id: int, db: Session = Depends(get_db)):
    record = db.query(AnalysisLog).filter(AnalysisLog.id == analysis_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Analysis not found")
    return record

@router.get("/analyses/{analysis_id}/file")
def get_analysis_csv(analysis_id: int, db: Session = Depends(get_db)):
    record = db.query(AnalysisLog).filter(AnalysisLog.id == analysis_id).first()
    if not record or not record.csv_text:
        raise HTTPException(status_code=404, detail="file not found")
    return Response(
        content=record.csv_text,
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename=analysis_{analysis_id}.csv"}
    )
