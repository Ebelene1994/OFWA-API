from fastapi.testclient import TestClient
from app.main import app
from io import BytesIO

client = TestClient(app)

def test_analyze_endpoint_valid():
    csv_content = b"city,region,sites\nA,R1,5\nB,R2,15\n"
    f = BytesIO(csv_content)
    response = client.post(
        "/analyze",
        files={"file": ("data.csv", f, "text/csv")},
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
