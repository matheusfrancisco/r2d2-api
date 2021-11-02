from fastapi.testclient import TestClient
from mangum import Mangum

from app.api import app, handler

client = TestClient(app)


def test_load_docs():
    response = client.get("/docs")
    assert response.status_code == 200


def test_handler():
    assert isinstance(handler, Mangum)

