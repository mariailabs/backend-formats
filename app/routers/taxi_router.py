from fastapi import APIRouter, status, HTTPException, Depends
from models.database import  get_db
from models import querys
from schemas.schemas import TaxiBase
from security.auth import get_current_user
from sqlalchemy.orm import Session
from typing import Annotated, List

router = APIRouter(
    prefix='/taxi',
    tags=['taxi']
)

@router.get("/", response_model=List[TaxiBase])
def read_exercises(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    exercises = querys.get_tarifs(db)
    if not exercises:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay tarifas")
    return exercises
