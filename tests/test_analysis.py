import pandas as pd
import pytest
from app.services.analysis import analyze_data

def test_analysis_normal():
    df = pd.DataFrame({
        "city": ["A", "B"],
        "region": ["R1", "R2"],
        "sites": [5, 15]
    })
    result = analyze_data(df, threshold=10)
    assert result["total_sites"] == 20
    assert result["top_region"] == "R2"
    assert result["cities_above_threshold"] == ["B"]
    assert result["average_sites_per_region"] == 10.0

def test_analysis_empty():
    df = pd.DataFrame(columns=["city","region","sites"])
    with pytest.raises(ValueError):
        analyze_data(df, threshold=5)

def test_analysis_high_threshold():
    df = pd.DataFrame({
        "city": ["A", "B"],
        "region": ["R1", "R2"],
        "sites": [5, 15]
    })
    result = analyze_data(df, threshold=100)
    assert result["cities_above_threshold"] == []
