from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db
import crud
import schemas


router = APIRouter(
    prefix="/characters",
    tags=["Characters"]
)


# GET

@router.get("/characteres/", response_model=list[schemas.Characteres])
def read_characteres(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    characteres = crud.get_characteres(db, skip=skip, limit=limit)
    return characteres


# POST

@router.post("/{user_id}/", response_model=schemas.Characteres)
def create_characteres_for_user(
    user_id: int, charactere: schemas.CharacteresCreate, db: Session = Depends(get_db)
):
    return crud.create_user_characteres(db=db, charactere=charactere, user_id=user_id)

# PACTH


@router.patch("/{charactere_id}/", response_model=schemas.Characteres)
def update_characteres(
    charactere_id: int, charactere: schemas.CharacteresUpdate, db: Session = Depends(get_db)
):
    return crud.update_characteres(db=db, charactere_id=charactere_id, charactere=charactere)


# DELETE

@router.delete("/{charactere_id}/", response_model=schemas.Characteres)
def delete_characteres(
    charactere_id: int, db: Session = Depends(get_db)
):
    return crud.delete_characteres(db=db, charactere_id=charactere_id)
