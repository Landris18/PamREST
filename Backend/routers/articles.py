from fastapi import APIRouter, Depends, HTTPException
from controllers.exceptions import ArticleException
from schemas import schemas
from db.database import get_db
from sqlalchemy.orm import Session
from controllers.controllers import ArticleController


router = APIRouter(
    prefix="/articles",
    tags=["Articles"],
)


class Articles:
    session : Session = Depends(get_db)

    @router.get("/get_articles", response_model = schemas.PaginatedArticle, summary = "Récupération des articles mis en avant")
    async def get_articles(limit: int = 2, offset: int = 0, db : Session = Depends(get_db)):
        try:
            articles = ArticleController.get_articles(limit, offset, db)
            response = {"limit": limit, "offset": offset, "data": articles}
            return response
        except Exception: 
            raise HTTPException(status_code=400, detail = "Impossible de récupérer les articles mis en avant")
            
            
    @router.get("/read_article/{_id}", response_model=schemas.Article, summary="Lecture d'un article")
    def read_article(_id: int, db : Session = Depends(get_db)):
        try:
            article = ArticleController.read_article(_id, db)
            return article
        except ArticleException as e:
            raise HTTPException(**e.__dict__)
    
