import pandas as pd
import os

SUPPORTED_EXTENSIONS = {".csv", ".xlsx", ".xls", ".json"}

def load_file(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        raise FileNotFoundError("Dataset file not found")

    ext = os.path.splitext(file_path)[1].lower()

    if ext not in SUPPORTED_EXTENSIONS:
        raise ValueError("Unsupported file format")

    if ext == ".csv":
        return pd.read_csv(file_path)

    if ext in {".xlsx", ".xls"}:
        return pd.read_excel(file_path)

    if ext == ".json":
        return pd.read_json(file_path)
