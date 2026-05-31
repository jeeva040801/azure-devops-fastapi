from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():

    response = client.get("/")

    assert response.status_code == 200

def test_prediction():

    response = client.post(
        "/predict",
        json={"area": 1200}
    )

    assert response.status_code == 200

    data = response.json()

    assert "predicted_price" in data
