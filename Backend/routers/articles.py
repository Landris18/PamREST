from fastapi import APIRouter, Depends, HTTPException
from dependencies import get_token_header
from models import models
from schemas import schemas
from db.database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)


router = APIRouter(
    prefix="/articles",
    tags=["articles"],
    dependencies=[Depends(get_token_header)]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()