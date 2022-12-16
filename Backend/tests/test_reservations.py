import sys, os
sys.path.insert(0, os.path.dirname('/'.join(__file__.split('/')[:-1])))

from fastapi.testclient import TestClient
from main import pam_rest
from os import environ as env
from dotenv import load_dotenv
from datetime import datetime, timedelta


load_dotenv()


client = TestClient(pam_rest)

id_reservation : int


def test_create_reservation_bad_token():
    response = client.post(
        "/reservations/create_reservation",
        headers={"jwt-token": "Bad_token"},
        json={
            "nom" : "Lionel",
            "prenom" : "Test",
            "mail" : "landry@gmail.com",
            "telephone" : "0348121147",
            "date" : "2008-06-10",
            "heure" : "20:10",
            "nombre" : 2
        }
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "JWT Token header invalid"}


def test_create_reservation_invalid():
    response = client.post(
        "/reservations/create_reservation",
        headers={"jwt-token": env.get("JWT_TOKEN")},
        json={"invalid_key": "data", "invalid_data": "key"},
    )
    assert response.status_code == 400
    assert response.json() is not None
    
    
def test_create_reservation_valid():
    tomorrow = datetime.now() + timedelta(days=1)
    tomorrow_date = tomorrow.strftime("%Y-%m-%d")
    
    response = client.post(
        "/reservations/create_reservation",
        headers={"jwt-token": env.get("JWT_TOKEN")},
        json={
            "nom" : "Lionel",
            "prenom" : "Test",
            "mail" : "landry@gmail.com",
            "telephone" : "0348121147",
            "date" : tomorrow_date,
            "heure" : "20:10",
            "nombre" : 2
        }
    )
    
    global id_reservation
    id_reservation = response.json()["id"]
    
    assert response.status_code == 201
    assert response.json() == {
        "nom" : "Lionel",
        "prenom" : "Test",
        "mail" : "landry@gmail.com",
        "telephone" : "0348121147",
        "date" : tomorrow_date,
        "heure" : "20:10:00",
        "nombre" : 2,
        "statut" : "reservée",
        "id" : id_reservation
    }


def test_edit_statut_reservation_bad_token():
    response = client.put(
        "/reservations/edit_statut_reservation/1/?new_statut=annulée",
        headers={"jwt-token": "Bad_token"}
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "JWT Token header invalid"}
    

def test_edit_statut_reservation_invalid_data():
    response = client.put(
        "/reservations/edit_statut_reservation/1/",
        headers={"jwt-token": env.get("JWT_TOKEN")},
    )
    assert response.status_code == 400
    assert response.json() is not None
    

def test_edit_statut_reservation_not_found():
    response = client.put(
        "/reservations/edit_statut_reservation/404/?new_statut=annulée",
        headers={"jwt-token": env.get("JWT_TOKEN")}
    )
    assert response.status_code == 404
    assert response.json() == {'detail': 'Reservation Not Found'}
    

def test_edit_statut_reservation_found():
    response = client.put(
        "/reservations/edit_statut_reservation/"+str(id_reservation)+"/?new_statut=annulée",
        headers={"jwt-token": env.get("JWT_TOKEN")}
    )
    assert response.status_code == 201
    assert response.json() is not None
    
    
def test_delete_reservation_bad_token():
    response = client.delete(
        "/reservations/delete_reservation/12",
        headers={"jwt-token": "Bad_token"}
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "JWT Token header invalid"}
    
    
def test_delete_reservation_not_found():
    response = client.delete(
        "/reservations/delete_reservation/404",
        headers={"jwt-token": env.get("JWT_TOKEN")}
    )
    assert response.status_code == 404
    assert response.json() == {'detail': 'Reservation Not Found'}
    

def test_delete_reservation_found():
    response = client.delete(
        "/reservations/delete_reservation/"+str(id_reservation),
        headers={"jwt-token": env.get("JWT_TOKEN")}
    )
    assert response.status_code == 200
    assert response.json() ==  {"message": "Reservation supprimée"}


def test_get_all_reservations():
    response = client.get("/reservations/get_all_reservations")   
    assert response.status_code == 200
    assert response.json() is not None
