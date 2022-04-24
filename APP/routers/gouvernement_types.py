from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db
import crud
import schemas


router = APIRouter(
    prefix="/gouvernement_types",
    tags=["Gouvernement Types"]
)


# GET

@router.get('/', response_model=list[schemas.GouvernementTypes])
def get_gouvernement_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    gouvernement_types = crud.get_gouvernement_types(db, skip=skip, limit=limit)
    return gouvernement_types


# POST

@router.post('/', response_model=schemas.GouvernementTypes)
def create_gouvernement_types(gouvernement_types: schemas.GouvernementTypesCreate, db: Session = Depends(get_db)):
    return crud.create_gouvernement_types(db=db, gouvernement_type=gouvernement_types)


# PATCH

@router.patch('/{gouvernement_types_id}', response_model=schemas.GouvernementTypes)
def update_gouvernement_types(gouvernement_type_id: int, gouvernement_types: schemas.GouvernementTypesUpdate, db: Session = Depends(get_db)):
    return crud.update_gouvernement_types(db=db, gouvernement_type_id=gouvernement_type_id, gouvernement_type=gouvernement_types)


# DELETE

@router.delete('/{gouvernement_type_id}', response_model=schemas.GouvernementTypes)
def delete_gouvernement_types(gouvernement_type_id: int, db: Session = Depends(get_db)):
    return crud.delete_gouvernement_types(db=db, gouvernement_type_id=gouvernement_type_id)
