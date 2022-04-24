from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dependencies import get_db
import crud
import schemas


router = APIRouter(
    prefix="/powers",
    tags=["Powers"],
)


# GET

@router.get('/', response_model=list[schemas.Powers])
def read_powers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    powers = crud.get_powers(db, skip=skip, limit=limit)
    return powers


# POST

@router.post('/', response_model=schemas.Powers)
def create_powers(powers: schemas.PowersCreate, db: Session = Depends(get_db)):
    return crud.create_powers(db=db, powers=powers)


# PATCH

@router.patch('/{powers_id}/', response_model=schemas.Powers)
def update_powers(powers_id: int, powers: schemas.PowersUpdate, db: Session = Depends(get_db)):
    return crud.update_powers(db=db, powers_id=powers_id, powers=powers)


# DELETE

@router.delete('/{powers_id}/', response_model=schemas.Powers)
def delete_powers(powers_id: int, db: Session = Depends(get_db)):
    return crud.delete_powers(db=db, powers_id=powers_id)
