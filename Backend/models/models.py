from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, BigInteger, Date, Time
from sqlalchemy.orm import relationship
from .database import Base
import enum


class Categorie(str, enum.Enum):
    starter = "Starter"
    main = "Main"
    pastry_drink = "Pastry and drink"
    

class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, unique=True, index=True)
    categorie = Column(Enum(Categorie))
    prix = Column(Integer, index=True)
    description = Column(String, index=True)
    image = Column(String, index=True)
    is_avant = Column(Boolean, default=False)
    

class Statut(int, enum.Enum):
    annulee = 0
    reservee = 1


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
    statut = Column(Enum(Statut))