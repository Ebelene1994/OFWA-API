import pandas as pd
import pytest
from app.services.normalizer import normalize_columns

def test_normalize_standard_columns():
    df = pd.DataFrame({
        "city": ["A"],
        "region": ["R1"],
        "sites": [10]
    })
    normalized = normalize_columns(df)
    assert list(normalized.columns) == ["city", "region", "sites"]

def test_normalize_alternate_columns():
    df = pd.DataFrame({
        "City": ["A"],
        "Region": ["R1"],
        "site_count": [5]
    })
    normalized = normalize_columns(df)
    assert list(normalized.columns) == ["city", "region", "sites"]

def test_missing_columns():
    df = pd.DataFrame({
        "city": ["A"],
        "sites": [5]
    })
    with pytest.raises(ValueError):
        normalize_columns(df)
