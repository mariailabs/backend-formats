from sqlalchemy.orm import Session
from . import models
from schemas.schemas import ClientBase

def get_tarifs(db: Session):
    return db.query(models.Taxi)

def get_client(db: Session):
    return db.query(models.Client)

def create_client(db: Session, client: ClientBase):
    db_client = models.Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client