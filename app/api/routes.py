from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session
import os
import shutil

from app.database import SessionLocal
from app.services.file_loader import load_file
from app.services.normalizer import normalize_columns
from app.services.analysis import analyze_data
from app.services.logger import save_analysis_log
from app.models.analysis import AnalysisLog

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/analyze")
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

        return save_analysis_log(db, file.filename, results)

    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))

@router.get("/analyses")
def get_all_analyses(db: Session = Depends(get_db)):
    return db.query(AnalysisLog).all()
