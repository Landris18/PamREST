from pydantic import BaseModel
from models.models import Categorie, Statut
import datetime


class MenuBase(BaseModel):
    nom : str
    categorie : Categorie
    prix : int
    description : str
    is_avant : bool
    
    
class Menu(MenuBase):
    id : int
    
    class Config:
        orm_mode = True


class PaginatedMenu(BaseModel):
    limit: int
    offset: int
    data: list[Menu]
    


class ReservationBase(BaseModel):
    nom : str
    prenom : str
    mail : str
    telephone : str
    date : datetime.date
    heure : datetime.time
    nombre : int
    statut : Statut
    
    
class Reservation(ReservationBase):
    id : int
    
    class Config:
        orm_mode = True



class ArticleBase(BaseModel):
    titre : str
    paragraphe : str
    image : str
    publicateur : str
    image_publicateur : str
    date : datetime.date
    heure : datetime.time
    nombre_commentaire : int
    is_avant : bool
    
    
class Article(ArticleBase):
    id : int
    
    class Config:
        orm_mode = True

class PaginatedArticle(BaseModel):
    limit: int
    offset: int
    data: list[Article]