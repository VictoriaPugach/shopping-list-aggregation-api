import json
from pathlib import Path

from fastapi.testclient import TestClient
import pytest

from src import aggregator
from src.api import app
from src.models import CONTRACT_VERSION

ROOT = Path(__file__).resolve().parents[1]
client = TestClient(app)


def request_payload() -> dict:
    return json.loads((ROOT / "data/aggregate-request.json").read_text())


def test_health_identifies_recipe_contract_version():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "recipe_contract_version": CONTRACT_VERSION}


def test_aggregate_accepts_shared_recipe_and_reports_scaffold_state():
    response = client.post("/aggregate", json=request_payload())
    assert response.status_code == 501
    assert response.json()["detail"]["code"] == "aggregation_not_implemented"


@pytest.mark.parametrize("payload", [{}, {"recipes": []}, {"recipes": [{"title": "missing contract"}]}, {"recipes": [], "extra": True}])
def test_aggregate_rejects_invalid_input(payload):
    assert client.post("/aggregate", json=payload).status_code == 422


def test_aggregate_passes_validated_recipes_to_service(monkeypatch):
    received = []

    def aggregate(recipes):
        received.extend(recipes)
        return {"items": [], "unresolved": []}

    monkeypatch.setattr(aggregator, "aggregate_recipes", aggregate)
    response = client.post("/aggregate", json=request_payload())
    assert response.status_code == 200
    assert response.json() == {"items": [], "unresolved": []}
    assert len(received) == 1
    assert received[0].schema_version == CONTRACT_VERSION
