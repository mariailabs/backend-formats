from fastapi import APIRouter, status, HTTPException, Depends
from schemas.schemas import ClientBase
from models.database import get_db
from models import querys
from security.auth import get_current_user
from sqlalchemy.orm import Session
from typing import  List

router = APIRouter(
    prefix='/client',
    tags=['client']
)

@router.get("/", response_model=List[ClientBase])
def read_client(db: Session = Depends(get_db)):
    exercises = querys.get_client(db)
    if not exercises:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay clientes")
    return exercises

@router.post("/", response_model=ClientBase)
def create_client(client: ClientBase, db: Session = Depends(get_db)):
    return querys.create_client(db, client)

@router.get("/{doc}", response_model=ClientBase)
def get_client_by_doc(doc: str,  db: Session = Depends(get_db)):
    return querys.find_by_doc(db, doc)