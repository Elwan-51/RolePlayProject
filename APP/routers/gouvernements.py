from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db
import crud
import schemas


router = APIRouter(
    prefix="/gouvernements",
    tags=["Gouvernements"]
)


# GET

@router.get('/', response_model=list[schemas.Gouvernement])
def get_gouvernements(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    gouvernements = crud.get_gouvernements(db, skip=skip, limit=limit)
    return gouvernements


# POST

@router.post('/', response_model=schemas.Gouvernement)
def create_gouvernement(gouvernement: schemas.GouvernementCreate, db: Session = Depends(get_db)):
    return crud.create_gouvernement(db=db, gouvernement=gouvernement)


# PATCH

@router.patch('/{gouvernements_id}', response_model=schemas.Gouvernement)
def update_gouvernement(gouvernements_id: int, gouvernement: schemas.GouvernementUpdate, db: Session = Depends(get_db)):
    return crud.update_gouvernement(db=db, gouvernement_id=gouvernements_id, gouvernement=gouvernement)


# DELETE

@router.delete('/{gouvernements_id}', response_model=schemas.Gouvernement)
def delete_gouvernement(gouvernements_id: int, db: Session = Depends(get_db)):
    return crud.delete_gouvernement(db=db, gouvernement_id=gouvernements_id)
