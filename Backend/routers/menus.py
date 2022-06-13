from fastapi import APIRouter, Depends, HTTPException
# from dependencies import get_token_header
from models import models
from schemas import schemas
from db.database import SessionLocal, engine
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)


router = APIRouter(
    prefix="/menus",
    tags=["menus"],
    # dependencies=[Depends(get_token_header)]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/get_all_menus", response_model=list[schemas.Menu])
def get_all_menus(db: Session = Depends(get_db)):
    menus = db.query(models.Menu).all()
    return menus

