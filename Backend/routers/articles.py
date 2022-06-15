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


@router.get("/get_articles", response_model=schemas.PaginatedArticle, summary="Récupération des articles mis en avant")
async def get_articles(response: Response, db: Session = Depends(get_db), offset: int = 0, limit: int = 2):
    try:
        articles = db.query(models.Article).filter(models.Article.is_avant == True).offset(offset).limit(limit).all()
        response.status_code = status.HTTP_200_OK
        return {"limit": limit, "offset": offset, "data": articles}
    except Exception:
        raise HTTPException(status_code=400, detail="Impossible de récupérer les articles mis en avant")
    
    
@router.get("/read_article/{_id}", response_model=schemas.Article, summary="Lecture d'un article")
def read_article(response: Response, _id: int, db: Session = Depends(get_db)):
    try:
        article = db.query(models.Article).get(_id)
        
        if article is None:
            response.status_code = status.HTTP_404_NOT_FOUND
            return article
        
        response.status_code = status.HTTP_200_OK
        return article
    except Exception:
        raise HTTPException(status_code=400, detail="Impossible de lire l'article")
    
