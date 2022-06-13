from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, BigInteger, Date, Time
from sqlalchemy.orm import relationship
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
    nom = Column(String, unique=True, index=True)
    categorie = Column(ENUM(Categorie))
    prix = Column(Integer, index=True)
    description = Column(String, index=True)
    image = Column(String, index=True)
    is_avant = Column(Boolean, default=False)
    

class Statut(str, enum.Enum):
    annulee = "reservée"
    reservee = "annulée"


class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    prenom = Column(String, index=True)
    mail = Column(String, index=True)
    telephone = Column(String, index=True)
    date = Column(Date)
    heure = Column(Time)
    nombre = Column(Integer, index=True)
    statut = Column(ENUM(Statut))
    
    
class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String, index=True)
    paragraphe = Column(String, index=True)
    image = Column(String, index=True)
    publicateur = Column(String, index=True)
    image_publicateur = Column(String, index=True)
    date = Column(Date)
    heure = Column(Time)
    nombre_commentaire = Column(Integer, index=True)