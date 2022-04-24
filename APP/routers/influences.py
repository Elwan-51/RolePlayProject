from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db
import crud
import schemas


router = APIRouter(
    prefix="/influences",
    tags=["Influences"]
)


# GET

@router.get('/', response_model=list[schemas.Influences])
def read_influences(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    influences = crud.get_influences(db, skip=skip, limit=limit)
    return influences


# POST

@router.post('/', response_model=schemas.Influences)
def create_influences(influences: schemas.InfluencesCreate, db: Session = Depends(get_db)):
    return crud.create_influences(db=db, influences=influences)


# PATCH

@router.patch('/{influence_id}', response_model=schemas.Influences)
def update_influences(influence_id: int, influences: schemas.InfluencesUpdate, db: Session = Depends(get_db)):
    return crud.update_influences(db=db, influences_id=influence_id, influences=influences)


# DELETE

@router.delete('/{influence_id}', response_model=schemas.Influences)
def delete_influences(influence_id: int, db: Session = Depends(get_db)):
    return crud.delete_influences(db=db, influences_id=influence_id)
