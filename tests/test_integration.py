from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

client = TestClient(app)

def fake_info(address: str):
    return {
        "address": address,
        "balance_trx": 123.45,
        "bandwidth_used": 10,
        "bandwidth_limit": 1000,
        "energy_used": 5,
        "energy_limit": 5000,
    }

@patch("app.tron_service.get_wallet_info", side_effect=fake_info)
def test_post_and_get(mock_service):
    addr = "TGzzB15h8YHHkeeEYoqEhK4nMxuU3cje6k"

    # POST
    r = client.post("/wallet-info", json={"address": addr})
    assert r.status_code == 200
    assert r.json()["balance_trx"] == 123.45

    # GET
    r2 = client.get("/requests?limit=1")
    body = r2.json()
    assert body["total"] >= 1
    assert body["items"][0]["wallet_address"] == addr
