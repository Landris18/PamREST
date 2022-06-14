import sys, os
sys.path.insert(0, os.path.dirname('/'.join(__file__.split('/')[:-1])))

from fastapi.testclient import TestClient
from main import pam_rest

client = TestClient(pam_rest)


def test_get_menus():
    response = client.get("/menus/get_menus")   
    assert response.status_code == 200
    assert response.json()["data"] is not None

