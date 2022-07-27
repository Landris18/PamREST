from pydantic import BaseModel, FutureDate, Field, validator, EmailStr, root_validator
from models.models import Categorie, Statut
import datetime


def heure_reservation_validator(heure_reservation: datetime.time):
    if heure_reservation >= datetime.time(8,30) and heure_reservation <= datetime.time(22,00):
        return heure_reservation
    raise ValueError("L'heure de la reservation doit être entre 8:30 et 22:00")


    
### Schemas for menu ###

class MenuBase(BaseModel):
    nom : str = Field(max_length = 50)
    categorie : Categorie
    prix : int = Field(
        gt = 0, lt=1000, 
        description = "The price must be greater than zero and inferior to 1000"
    )
    description : str = Field(max_length = 250)
    is_avant : bool
    
    
class Menu(MenuBase):
    id : int
    
    class Config:
        orm_mode = True
        

class PaginatedMenu(BaseModel):
    limit: int
    offset: int
    data: list[Menu]
    
    
    
### Schemas for reservation ###

class ReservationCreate(BaseModel):
    nom : str = Field(max_length = 50)
    prenom : str = Field(max_length = 50)
    mail : EmailStr = Field()
    telephone : str = Field(max_length = 15)
    date : FutureDate
    heure : datetime.time
    nombre : int = Field(
        lt = 20, 
        description = "Number of persons in one reservation must be ineferior to 20"
    )
    
    # Validator
    _validate_heure = validator('heure', allow_reuse=True)(heure_reservation_validator)
    
    
class ReservationBase(BaseModel):
    nom : str = Field(max_length = 50)
    prenom : str = Field(max_length = 50)
    mail : EmailStr = Field()
    telephone : str = Field(max_length = 15)
    date : FutureDate
    heure : datetime.time
    nombre : int = Field(
        lt = 20, 
        description = "Number of persons in one reservation must be ineferior to 20"
    )
    statut : Statut
    
    # Validator
    _validate_heure = validator('heure', allow_reuse=True)(heure_reservation_validator)
    
    
class Reservation(ReservationBase):
    id : int
    
    class Config:
        orm_mode = True



### Schemas for article ###

class ArticleBase(BaseModel):
    titre : str = Field(max_length = 100)
    paragraphe : str = Field(max_length = 250)
    image : str = Field(max_length = 250)
    publicateur : str = Field(max_length = 50)
    image_publicateur : str = Field(max_length = 250)
    date : datetime.date
    heure : datetime.time
    nombre_commentaire : int
    is_avant : bool
    
    @validator("image", "image_publicateur")
    def url_must_constains_https(cls, value):
        if "https" not in value:
            raise ValueError("Image url must conatains https")
        return value
    
    @root_validator
    def date_heure_article_validator(cls, values):
        date, time = values.get('date'), values.get('heure')
        if datetime.datetime.combine(date, time) <= datetime.datetime.now():
            return values
        raise ValueError("La date de publication de l'article ne doit pas dépasser maintenant")
    
    
class Article(ArticleBase):
    id : int
    
    class Config:
        orm_mode = True


class PaginatedArticle(BaseModel):
    limit: int
    offset: int
    data: list[Article]
