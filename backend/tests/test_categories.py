from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_categories():
    response = client.get("/categories")
    assert response.status_code == 200
