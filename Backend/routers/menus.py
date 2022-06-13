from fastapi import APIRouter, Depends, HTTPException, Request, status, Response
# from dependencies import get_token_header
from models import models
from schemas import schemas
from db.database import get_db, engine
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)


router = APIRouter(
    prefix="/menus",
    tags=["Menus"],
    # dependencies=[Depends(get_token_header)]
)


@router.get("/get_all_menus", response_model=list[schemas.Menu], summary="Récupération de tous les menus")
def get_all_menus(response: Response, db: Session = Depends(get_db)):
    try:
        menus = db.query(models.Menu).all()
        response.status_code = status.HTTP_200_OK
        return menus
    except Exception:
        raise HTTPException(status_code=400, detail="Impossible de récupérer la liste des menus")

