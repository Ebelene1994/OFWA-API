from fastapi import APIRouter, HTTPException, status
from sqlalchemy import text
from app.database import engine

router = APIRouter()

@router.get("/health", status_code=status.HTTP_200_OK)
def health():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
    except Exception:
        raise HTTPException(status_code=503, detail="Database connection failed")

    return {"status": "ok", "api": "ok", "database": "ok"}
