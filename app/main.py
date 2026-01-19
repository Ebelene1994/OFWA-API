from fastapi import FastAPI
from sqlalchemy import text
from app.api.routes import router
from app.database import Base, engine
from app.api.health import router as health_router

Base.metadata.create_all(bind=engine)

# Ensure sqlite schema has the csv_text column (simple in-place migration for SQLite)
def ensure_sqlite_schema():
    try:
        with engine.connect() as conn:
            cols = {row[1] for row in conn.execute(text("PRAGMA table_info('analysis_logs')"))}
            if 'csv_text' not in cols:
                conn.execute(text("ALTER TABLE analysis_logs ADD COLUMN csv_text TEXT"))
    except Exception:
        # Best-effort; ignore if table does not exist yet
        pass

ensure_sqlite_schema()

app = FastAPI(
    title="OFWA API",
    description="FastAPI service for uploading a dataset, normalizing its columns, running analytics, and logging results to a local SQLite database.",
    version="1.0.0"
)

app.include_router(health_router)
app.include_router(router)
