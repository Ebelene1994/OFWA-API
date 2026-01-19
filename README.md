# OFWA API

FastAPI service for uploading a dataset, normalizing its columns, running analytics, and logging results to a local SQLite database.

Endpoints:

- `POST /analyze` Upload and analyze a dataset file.
- `GET /analyses` List saved analysis logs.
- `GET /analyses/{id}` Get a single analysis log.
- `GET /analyses/{id}/csv` Download the stored normalized CSV.

Request details:

- `POST /analyze`
  - Content-Type: `multipart/form-data`
  - Fields:
    - `file`: required (CSV/XLSX/XLS/JSON)
    - `threshold`: optional integer (default: 10)
  - Response: analysis record (use `/analyses/{id}/csv` to get the CSV content)

## Prerequisites

- Python 
- pip 

## Setup

1. Create and activate a virtual environment (recommended):
   - venv (Windows):
     - `python -m venv .venv`
     - `.venv\\Scripts\\activate`

2. Install dependencies:
   - `pip install -r requirements.txt`

## Run the API

Start the development server:

- `fastapi dev`

Alternative:

- `uvicorn app.main:app --reload`

Open the interactive docs:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

Notes:

- A local SQLite DB file `analysis_logs.db` is created automatically in the project root.
- Uploaded files are stored in the `uploads/` directory.
- Supported input formats: `.csv`, `.xlsx`, `.xls`, `.json`.
- The normalized CSV is stored in the database (`csv_text`) and available via `GET /analyses/{id}/csv`.
- On startup, the app will auto-add the `csv_text` column to an existing SQLite DB if it's missing.

### Example requests

Analyze a local CSV and then download its stored CSV:

```bash
curl -X POST \
  -F "file=@path/to/data.csv" \
  -F "threshold=10" \
  http://127.0.0.1:8000/analyze

# then, assuming the response had "id": 1
curl -L -o analysis_1.csv http://127.0.0.1:8000/analyses/1/csv
```

## Run the tests

This project uses `pytest`.

- Run all tests (From project root):
  - `pytest --maxfail=1 --disable-warnings -q`
- Run with concise output:
  - `pytest -q`
- Run a specific test file:
  - `pytest tests/test_analysis.py -q`


