from fastapi import HTTPException
from typing import List
from models import models
from sqlalchemy.orm import Session
from .exceptions import ArtcileNotFoundError,ReservationNotFoundError
from db.database import engine
from schemas import schemas


models.Base.metadata.create_all(bind=engine)


class ArticleController:
    
    def get_articles(limit: int, offset: int, db: Session) -> List[models.Article]:
        """
            DESC: Fonction permettant la récupération des articles mis en avant
        """
        articles = db.query(models.Article).filter(models.Article.is_avant == True).offset(offset).limit(limit).all()
        return articles
    

    def read_article(_id: int, db: Session) -> models.Article:
        """
            DESC: Fonction permettant la lecture d'une article
        """
        article = db.query(models.Article).get(_id)
        
        if article is None:
            raise ArtcileNotFoundError
        
        return article


class MenuController:
    
    def get_menus(limit: int, offset: int, db: Session) -> List[models.Menu]:
        """
            DESC: Fonction permettant la récupération des menus mis en avant
        """
        menus = db.query(models.Menu).filter(models.Menu.is_avant == True).offset(offset).limit(limit).all()
        return menus


    def get_all_starters(db: Session) -> List[models.Menu]:
        """
            DESC: Fonction permettant la récupération de tous les starters
        """
        starters = db.query(models.Menu).filter(models.Menu.categorie == "Starter").all()
        return starters

        
    def get_all_mains(db: Session) -> List[models.Menu]:
        """
            DESC: Fonction permettant la récupération de tous les mains
        """
        mains = db.query(models.Menu).filter(models.Menu.categorie == "Main").all()
        return mains

    
    def get_all_pastries_and_drinks(db: Session) -> List[models.Menu]:
        """
            DESC: Fonction permettant la récupération de tous les pastries & drinks
        """
        pastries_drinks = db.query(models.Menu).filter(models.Menu.categorie == "Pastry & drink").all()
        return pastries_drinks


class ReservationController:
    
    def create_reservation(reservation: schemas.ReservationCreate, db:Session) -> models.Reservation:
        """
            DESC: Fonction permettant la création d'une reservation
        """
        reservation_to_create = models.Reservation(
           **reservation.dict()
        )
        reservation_to_create.statut = "reservée"
        
        db.add(reservation_to_create)
        db.commit()
        db.refresh(reservation_to_create)
        
        return reservation_to_create
    

    def edit_statut_reservation(_id: int, new_statut: str, db: Session) -> models.Reservation:
        """
            DESC: Modification de statut d'une reservation
        """
        reservation_exist = db.query(models.Reservation).get(_id)
        
        if reservation_exist is None:
            raise ReservationNotFoundError

        reservation_exist.statut = new_statut 
        db.commit()
        db.refresh(reservation_exist)
        
        return reservation_exist
    

    def delete_reservation(_id: int, db: Session) -> str:
        """
            DESC: Suppression d'une reservation
        """
        reservation_exist = db.query(models.Reservation).get(_id)
        
        if reservation_exist is None:
            raise ReservationNotFoundError

        db.delete(reservation_exist)
        db.commit()
        
        return {"message": "Reservation supprimée"}


    def get_all_reservations(db: Session) -> List[models.Reservation]:
        """
            DESC: Récupération de la liste de toutes les reservations
        """
        reservations = db.query(models.Reservation).all()
        return reservations