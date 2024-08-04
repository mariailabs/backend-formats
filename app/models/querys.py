from sqlalchemy.orm import Session
from . import models

def get_exercises(db: Session):
    return db.query(models.Taxi)