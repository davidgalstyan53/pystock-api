from fastapi.testclient import TestClient
from app.main import app
from app.config import Settings

client = TestClient(app)


def test_root_endpoint():
    settings = Settings()
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": f"Welcome to {settings.api_name}"}
