from fastapi import APIRouter, Depends, HTTPException, Request, status, Response
from models import models
from schemas import schemas
from db.database import get_db, engine
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)


router = APIRouter(
    prefix="/menus",
    tags=["Menus"]
)


@router.get("/get_menus", response_model=schemas.PaginatedMenu, summary="Récupération des menus mis en avant")
def get_menus(response: Response, db: Session = Depends(get_db), offset: int = 0, limit: int = 4):
    try:
        menus = db.query(models.Menu).filter(models.Menu.is_avant == True).offset(offset).limit(limit).all()
        response.status_code = status.HTTP_200_OK
        return {"limit": limit, "offset": offset, "data" : menus}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Impossible de récupérer les menus mis en avant")


@router.get("/get_all_starters", response_model=list[schemas.Menu], summary="Récupération de tous les starters")
def get_all_starters(response: Response, db: Session = Depends(get_db)):
    try:
        starters = db.query(models.Menu).filter(models.Menu.categorie == "Starter").all()
        response.status_code = status.HTTP_200_OK
        return starters
    except Exception:
        raise HTTPException(status_code=400, detail="Impossible de récupérer la liste des starters")
    

@router.get("/get_all_mains", response_model=list[schemas.Menu], summary="Récupération de tous les mains")
def get_all_mains(response: Response, db: Session = Depends(get_db)):
    try:
        mains = db.query(models.Menu).filter(models.Menu.categorie == "Main").all()
        response.status_code = status.HTTP_200_OK
        return mains
    except Exception:
        raise HTTPException(status_code=400, detail="Impossible de récupérer la liste des mains")
    

@router.get("/get_all_pastries_and_drinks", response_model=list[schemas.Menu], summary="Récupération de tous les pastries & drinks")
def get_menus(response: Response, db: Session = Depends(get_db)):
    try:
        pastries_drinks = db.query(models.Menu).filter(models.Menu.categorie == "Pastry & drink").all()
        response.status_code = status.HTTP_200_OK
        return pastries_drinks
    except Exception:
        raise HTTPException(status_code=400, detail="Impossible de récupérer la liste des pastries and drinks")
