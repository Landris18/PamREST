from fastapi import APIRouter, Depends, HTTPException
# from dependencies import get_token_header
from models import models
from schemas import schemas
from db.database import SessionLocal, engine
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)


router = APIRouter(
    prefix="/reservations",
    tags=["Reservations"],
    # dependencies=[Depends(get_token_header)]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
@router.get("/get_all_reservations", response_model=list[schemas.Reservation], summary="Récupération de toutes les réservations")
def get_all_reservations(db: Session = Depends(get_db)):
    reservations = db.query(models.Reservation).all()
    return reservations
