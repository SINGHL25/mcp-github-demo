
import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_get_repositories():
    response = client.post("/repos", json={"username": "octocat"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert "name" in data[0]
