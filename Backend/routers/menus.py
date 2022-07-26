from fastapi import APIRouter, Depends, HTTPException
from controllers.controllers import MenuController
from models import models
from schemas import schemas
from db.database import get_db, engine
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)


router = APIRouter(
    prefix="/menus",
    tags=["Menus"]
)


@router.get("/get_menus", summary="Récupération des menus mis en avant")
def get_menus(offset: int = 0, limit: int = 4, db: Session = Depends(get_db)):
    try:
        menus = MenuController.get_menus(limit, offset, db)
        response = {"limit": limit, "offset": offset, "data" : menus}
        return response
    except Exception:
        raise HTTPException(status_code=400, detail="Impossible de récupérer les menus mis en avant")


@router.get("/get_all_starters", response_model=list[schemas.Menu], summary="Récupération de tous les starters")
def get_all_starters(db: Session = Depends(get_db)):
    try:
        starters = MenuController.get_all_starters(db)
        return starters
    except Exception:
        raise HTTPException(status_code=400, detail="Impossible de récupérer la liste des starters")
    

@router.get("/get_all_mains", response_model=list[schemas.Menu], summary="Récupération de tous les mains")
def get_all_mains(db: Session = Depends(get_db)):
    try:
        mains = MenuController.get_all_mains(db)
        return mains
    except Exception:
        raise HTTPException(status_code=400, detail="Impossible de récupérer la liste des mains")
    

@router.get("/get_all_pastries_and_drinks", response_model=list[schemas.Menu], summary="Récupération de tous les pastries & drinks")
def get_all_pastries_and_drinks(db: Session = Depends(get_db)):
    try:
        pastries_drinks = MenuController.get_all_pastries_and_drinks(db)
        return pastries_drinks
    except Exception:
        raise HTTPException(status_code=400, detail="Impossible de récupérer la liste des pastries & drinks")
