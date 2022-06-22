from fastapi import APIRouter, Depends, HTTPException, status, Response
from dependencies import get_token_header
from models import models
from schemas import schemas
from db.database import get_db, engine
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/reservations",
    tags=["Reservations"],
)


@router.post(
    "/create_reservation", 
    response_model=schemas.Reservation, 
    summary="Création d'une reservation",
    dependencies=[Depends(get_token_header)]
)
def create_reservation(response: Response, reservation: schemas.ReservationCreate, db: Session = Depends(get_db)):
    try:
        reservation_to_create = models.Reservation(
            nom = reservation.nom, 
            prenom = reservation.prenom,
            mail = reservation.mail,
            telephone = reservation.telephone,
            date = reservation.date,
            heure = reservation.heure,
            nombre = reservation.nombre,
            statut = "reservée"
        )
        db.add(reservation_to_create)
        db.commit()
        db.refresh(reservation_to_create)
        
        response.status_code = status.HTTP_201_CREATED
        return reservation_to_create
    
    except Exception:
        raise HTTPException(status_code=400, detail="Impossible d'effectuer la reservation")
    
    
@router.put(
    "/edit_statut_reservation/{_id}/",
    response_model=schemas.Reservation, 
    summary="Modification de statut d'une reservation",    
    dependencies=[Depends(get_token_header)]
)
def edit_statut_reservation(response: Response, _id: int, new_statut: str, db: Session = Depends(get_db)):
    try:
        reservation_exist = db.query(models.Reservation).get(_id)
        
        if reservation_exist is None:
            response.status_code = status.HTTP_404_NOT_FOUND
            return reservation_exist

        reservation_exist.statut = new_statut 
        db.commit()
        db.refresh(reservation_exist)
        
        response.status_code = status.HTTP_201_CREATED
        return reservation_exist
    
    except Exception:
        raise HTTPException(status_code=400, detail="Impossible d'éditer le statut de la reservation")
    
    
@router.delete(
    "/delete_reservation/{_id}", 
    summary="Suppression d'une reservation",
    dependencies=[Depends(get_token_header)]
)
def delete_reservation(response: Response, _id: int, db: Session = Depends(get_db)):
    try:
        reservation_exist = db.query(models.Reservation).get(_id)
        
        if reservation_exist is None:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"message": "Reservation non trouvée"}

        db.delete(reservation_exist)
        db.commit()
        
        response.status_code = status.HTTP_200_OK
        return {"message": "Reservation supprimée"}
    
    except Exception:
        raise HTTPException(status_code=400, detail="Impossible de supprimer la reservation")
    
        
@router.get("/get_all_reservations", response_model=list[schemas.Reservation], summary="Récupération de toutes les réservations")
def get_all_reservations(response: Response, db: Session = Depends(get_db)):
    try:
        reservations = db.query(models.Reservation).all()
        response.status_code = status.HTTP_200_OK
        return reservations
    except Exception:
        raise HTTPException(status_code=400, detail="Impossible de récupérer la liste des reservations")
