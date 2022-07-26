from fastapi import APIRouter, Depends, HTTPException, status, Response
from requests import session
from controllers.controllers import ReservationController
from controllers.exceptions import ReservationException
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


class Reservations:

    session: Session = Depends(get_db)
    
    @router.post(
        "/create_reservation", 
        response_model=schemas.Reservation, 
        summary="Création d'une reservation",
        dependencies=[Depends(get_token_header)]
    )
    def create_reservation(response: Response, reservation: schemas.ReservationCreate, db: Session = Depends(get_db)):
        try:
            reservation_to_create = ReservationController.create_reservation(reservation, db)
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
            reservation_edit = ReservationController.edit_statut_reservation(_id, new_statut, db)
            response.status_code = status.HTTP_201_CREATED
            return reservation_edit
        except ReservationException as e:
            raise HTTPException(**e.__dict__)
        
        
    @router.delete(
        "/delete_reservation/{_id}", 
        summary="Suppression d'une reservation",
        dependencies=[Depends(get_token_header)]
    )
    def delete_reservation(_id: int, db: Session = Depends(get_db)):
        try:
            ReservationController.delete_reservation(_id, db)
            return {"message": "Reservation supprimée"}
        
        except ReservationException as e:
            raise HTTPException(**e.__dict__)
        
            
    @router.get("/get_all_reservations", response_model=list[schemas.Reservation], summary="Récupération de toutes les réservations")
    def get_all_reservations(db: Session = Depends(get_db)):
        try:
            reservations = ReservationController.get_all_reservations(db)
            return reservations
        except Exception:
            raise HTTPException(status_code=400, detail="Impossible de récupérer la liste des reservations")

