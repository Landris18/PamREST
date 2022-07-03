import sys, os
sys.path.insert(0, os.path.dirname('/'.join(__file__.split('/')[:-1])))

from fastapi.testclient import TestClient
from main import pam_rest


client = TestClient(pam_rest)


def test_get_articles():
    response = client.get("/articles/get_articles")   
    assert response.status_code == 200
    assert response.json()["data"] is not None


def test_read_article_not_found():
    response = client.get("/articles/read_article/404")   
    assert response.status_code == 404
    assert response.json() == None


# def test_read_article_found():
#     response = client.get("/articles/read_article/1")  
#     assert response.status_code == 200
#     assert response.json() is not None