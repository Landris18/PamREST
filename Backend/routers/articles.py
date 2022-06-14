from fastapi import APIRouter, Depends, HTTPException, Request, status, Response
from models import models
from schemas import schemas
from db.database import get_db, engine
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)


router = APIRouter(
    prefix="/articles",
    tags=["Articles"],
)


# response_model=list[schemas.Article]
@router.get("/get_articles", summary="Récupération des articles mis en avant")
async def get_articles(response: Response, db: Session = Depends(get_db), offset: int = 0, limit: int = 2):
    try:
        articles = db.query(models.Article).filter(models.Article.is_avant == True).offset(offset).limit(limit).all()
        response.status_code = status.HTTP_200_OK
        return articles
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Impossible de récupérer les articles mis en avant")
    
    
# response_model=schemas.Article   
@router.get("/read_article/{_id}", summary="Lecture d'un article")
def read_article(response: Response, _id: int, db: Session = Depends(get_db)):
    try:
        article = db.query(models.Article).get(_id)
        response.status_code = status.HTTP_200_OK
        return article
    except Exception:
        raise HTTPException(status_code=400, detail="Impossible de lire l'article")
    
