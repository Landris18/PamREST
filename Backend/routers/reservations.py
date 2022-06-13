from fastapi import APIRouter, Depends, HTTPException, Request, status, Response
# from dependencies import get_token_header
from models import models
from schemas import schemas
from db.database import get_db, engine
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)


router = APIRouter(
    prefix="/reservations",
    tags=["Reservations"],
    # dependencies=[Depends(get_token_header)]
)

        
@router.get("/get_all_reservations", response_model=list[schemas.Reservation], summary="Récupération de toutes les réservations")
def get_all_reservations(response: Response, db: Session = Depends(get_db)):
    try:
        reservations = db.query(models.Reservation).all()
        response.status_code = status.HTTP_200_OK
        return reservations
    except Exception:
        raise HTTPException(status_code=400, detail="Impossible de récupérer la liste des reservations")
