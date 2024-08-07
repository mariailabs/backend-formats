from sqlalchemy.orm import Session
from . import models

def get_exercises(db: Session):
    return db.query(models.Taxi)

def get_client(db: Session):
    return db.query(models.Client)