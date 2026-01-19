# OFWA API

FastAPI service for uploading a dataset, normalizing its columns, running analytics, and logging results to a local SQLite database.

Endpoints:

- `POST /analyze` Upload and analyze a dataset file.
- `GET /analyses` List saved analysis logs.

## Prerequisites

- Python 
- pip (or conda, optional)

## Setup

1. Create and activate a virtual environment (recommended):
   - venv (Windows):
     - `python -m venv .venv`
     - `.venv\\Scripts\\activate`
   - conda (optional):
     - `conda create -n ofwa-api python=3.10 -y`
     - `conda activate ofwa-api`

2. Install dependencies:
   - `pip install -r requirements.txt`

## Run the API

Start the development server:

- `fastapi dev`

Open the interactive docs:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

Notes:

- A local SQLite DB file `analysis_logs.db` is created automatically in the project root.
- Uploaded files are stored in the `uploads/` directory.
- Supported input formats: `.csv`, `.xlsx`, `.xls`, `.json`.

## Run the tests

This project uses `pytest`.

- Run all tests (From project root):
  - `pytest --maxfail=1 --disable-warnings -q`
`
- Run with concise output:
  - `pytest -q`
- Run a specific test file:
  - `pytest tests/test_analysis.py -q`

Test data note:

- The API test uses `data/galamsay_data.xlsx`. Ensure this file exists locally (or adjust the test path) before running `tests/test_api.py`.

