from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_analyze_endpoint_valid():
    with open("data/galamsay_data.xlsx", "rb") as f:
        response = client.post(
            "/analyze",
            files={"file": ("galamsay_data.xlsx", f)},
            data={"threshold": 10}
        )
    assert response.status_code == 200
    json_data = response.json()
    assert "total_sites" in json_data
    assert "top_region" in json_data
    assert "average_sites_per_region" in json_data

def test_analyze_endpoint_invalid_file():
    from io import BytesIO
    fake_file = BytesIO(b"random content")
    response = client.post(
        "/analyze",
        files={"file": ("fake.txt", fake_file)}
    )
    assert response.status_code == 400

def test_list_analyses_endpoint():
    response = client.get("/analyses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
