from fastapi import APIRouter, Depends, HTTPException, Request, status, Response
# from dependencies import get_token_header
from models import models
from schemas import schemas
from db.database import get_db, engine
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)


router = APIRouter(
    prefix="/articles",
    tags=["Articles"],
    # dependencies=[Depends(get_token_header)]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()