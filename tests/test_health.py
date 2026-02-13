from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_healthz_ok():
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_readyz_ok():
    r = client.get("/readyz")
    assert r.status_code == 200
    assert r.json()["ready"] is True

def test_version_fields_present():
    r = client.get("/version")
    assert r.status_code == 200
    data = r.json()
    assert "app" in data
    assert "git_commit" in data
    assert "build_time" in data
    assert "server_time_utc" in data