from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dependencies import get_db
import crud
import schemas


router = APIRouter(
    prefix="/locations",
    tags=["locations"]
)


# GET

@router.get('/', response_model=list[schemas.Location])
def get_locations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    locations = crud.get_locations(db, skip=skip, limit=limit)
    return locations


# POST

@router.post('/', response_model=schemas.Location)
def create_location(location: schemas.LocationCreate, db: Session = Depends(get_db)):
    return crud.create_location(db=db, location=location)


# PATCH

@router.patch('/{location_id}', response_model=schemas.Location)
def update_location(location_id: int, location: schemas.LocationUpdate, db: Session = Depends(get_db)):
    return crud.update_location(db=db, location_id=location_id, location=location)


# DELETE

@router.delete('/{location_id}', response_model=schemas.Location)
def delete_location(location_id: int, db: Session = Depends(get_db)):
    return crud.delete_location(db=db, location_id=location_id)