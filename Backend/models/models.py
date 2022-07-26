from sqlalchemy import Boolean, Column, Integer, String, Date, Time
from db.database import Base
import enum
from sqlalchemy.dialects.mysql import ENUM

class Categorie(str, enum.Enum):
    starter = "Starter"
    main = "Main"
    pastry_drink = "Pastry & drink"
    

class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(50), unique=True, index=True)
    categorie = Column(ENUM(Categorie))
    prix = Column(Integer, index=True)
    description = Column(String(250))
    is_avant = Column(Boolean, default=False, index=True)
    

class Statut(str, enum.Enum):
    annulee = "annulée"
    reservee = "reservée"


class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(50))
    prenom = Column(String(50))
    mail = Column(String(50))
    telephone = Column(String(15))
    date = Column(Date, index=True)
    heure = Column(Time)
    nombre = Column(Integer, index=True)
    statut = Column(ENUM(Statut), index=True)
    
    
class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String(100), index=True)
    paragraphe = Column(String(250))
    image = Column(String(250))
    publicateur = Column(String(50), index=True)
    image_publicateur = Column(String(250))
    date = Column(Date, index=True)
    heure = Column(Time)
    nombre_commentaire = Column(Integer, index=True)
    is_avant = Column(Boolean, default=False, index=True)