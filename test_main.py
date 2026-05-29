from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "message": "API is running"}

def test_read_item():
    response = client.get("/query/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "data": "Sample retrieved context"}
