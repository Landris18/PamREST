import sys, os
sys.path.insert(0, os.path.dirname('/'.join(__file__.split('/')[:-1])))

from fastapi.testclient import TestClient
from main import pam_rest


client = TestClient(pam_rest)


def test_get_menus():
    response = client.get("/menus/get_menus")   
    assert response.status_code == 200
    assert response.json()["data"] is not None


def test_get_all_starters():
    response = client.get("/menus/get_all_starters")   
    assert response.status_code == 200
    assert response.json() is not None
    
    
def test_get_all_mains():
    response = client.get("/menus/get_all_mains")   
    assert response.status_code == 200
    assert response.json() is not None
    
    
def test_get_all_pastries_and_drinks():
    response = client.get("/menus/get_all_pastries_and_drinks")   
    assert response.status_code == 200
    assert response.json() is not None