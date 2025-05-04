from fastapi.testclient import TestClient
from app import app  # Upewnij się, że masz from app import app
from settings import Settings

client = TestClient(app)  # To była brakująca linia!

def test_welcome():
    response = client.get("/")
    assert response.status_code == 200
    assert Settings().APP_NAME in response.json()["message"]

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "environment": Settings().ENVIRONMENT
    }