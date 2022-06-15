import sys, os
sys.path.insert(0, os.path.dirname('/'.join(__file__.split('/')[:-1])))

from fastapi.testclient import TestClient
from main import pam_rest


client = TestClient(pam_rest)


def test_get_get_headline_hero():
    response = client.get("/headers/get_headline_hero")   
    assert response.status_code == 200
    assert response.json() == {
        "titre" : "Healthy eating is important part of lifestyle", 
        "subtitle" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Neque congue arcu"
    }


def test_get_image_boxes():
    response = client.get("/headers/get_image_boxes")   
    assert response.status_code == 200
    assert response.json() ==  [
        {
            "image" : "",
            "description" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Neque congue arcu"
        },
        {
            "image" : "",
            "description" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Neque congue arcu"
        }
    ]
