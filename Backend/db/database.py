from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import environ as env
from dotenv import load_dotenv


load_dotenv()


SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://"+env.get("DB_USER")+":"+env.get("DB_PASSWORD")+"@"+env.get("DB_HOST")+":"+env.get("DB_PORT")+"/"+env.get("DB_NAME")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """
        DESC: Création d'une session pour la base de donnée
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()