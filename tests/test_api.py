from fastapi.testclient import TestClient

from app.api import app

client = TestClient(app)


def test_load_docs():
    response = client.get("/docs")
    assert response.status_code == 200
