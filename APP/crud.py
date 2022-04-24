from sqlalchemy.orm import Session

import models, schemas


# User

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(username=user.username, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise Exception("User not found")
    user_data = user.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(db_user, key, value)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise Exception("User not found")
    db_user_characteres = db.query(models.Charactere).filter(models.Charactere.owner_id == user_id).all()
    for db_user_charactere in db_user_characteres:
        db.delete(db_user_charactere)
    db.delete(db_user)
    db.commit()
    return db_user


# Characteres
def get_characteres(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Charactere).offset(skip).limit(limit).all()


def create_user_characteres(db: Session, charactere: schemas.CharacteresCreate, user_id: int):
    db_item = models.Charactere(**charactere.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_characteres(db: Session, charactere_id: int, charactere: schemas.CharacteresUpdate):
    db_charactere = db.query(models.Charactere).filter(models.Charactere.id == charactere_id).first()
    if not db_charactere:
        raise Exception("Charactere not found")
    charactere_data = charactere.dict(exclude_unset=True)
    for key, value in charactere_data.items():
        setattr(db_charactere, key, value)
    db.add(db_charactere)
    db.commit()
    db.refresh(db_charactere)
    return db_charactere


def delete_characteres(db: Session, charactere_id: int):
    db_charactere = db.query(models.Charactere).filter(models.Charactere.id == charactere_id).first()
    if not db_charactere:
        raise Exception("Charactere not found")
    db.delete(db_charactere)
    db.commit()
    return db_charactere


# Influences

def get_influences(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Influences).offset(skip).limit(limit).all()


def create_influences(db: Session, influences: schemas.InfluencesCreate):
    db_item = models.Influences(**influences.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_influences(db: Session, influences_id: int, influences: schemas.InfluencesUpdate):
    db_influences = db.query(models.Influences).filter(models.Influences.id == influences_id).first()
    if not db_influences:
        raise Exception("Influences not found")
    influences_data = influences.dict(exclude_unset=True)
    for key, value in influences_data.items():
        setattr(db_influences, key, value)
    db.add(db_influences)
    db.commit()
    db.refresh(db_influences)
    return db_influences


def delete_influences(db: Session, influences_id: int):
    db_influences = db.query(models.Influences).filter(models.Influences.id == influences_id).first()
    if not db_influences:
        raise Exception("Influences not found")
    db.delete(db_influences)
    db.commit()
    return db_influences


# Powers

def get_powers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Powers).offset(skip).limit(limit).all()


def create_powers(db: Session, powers: schemas.PowersCreate):
    db_item = models.Powers(**powers.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_powers(db: Session, powers_id: int, powers: schemas.PowersUpdate):
    db_powers = db.query(models.Powers).filter(models.Powers.id == powers_id).first()
    if not db_powers:
        raise Exception("Powers not found")
    powers_data = powers.dict(exclude_unset=True)
    for key, value in powers_data.items():
        setattr(db_powers, key, value)
    db.add(db_powers)
    db.commit()
    db.refresh(db_powers)
    return db_powers


def delete_powers(db: Session, powers_id: int):
    db_powers = db.query(models.Powers).filter(models.Powers.id == powers_id).first()
    if not db_powers:
        raise Exception("Powers not found")
    db.delete(db_powers)
    db.commit()
    return db_powers


# GouvernementTypes

def get_gouvernement_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.GouvernementType).offset(skip).limit(limit).all()


def create_gouvernement_types(db: Session, gouvernement_type: schemas.GouvernementTypesCreate):
    db_item = models.GouvernementType(**gouvernement_type.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_gouvernement_types(db: Session, gouvernement_type_id: int, gouvernement_type: schemas.GouvernementTypesUpdate):
    db_gouvernement_type = db.query(models.GouvernementType).filter(models.GouvernementType.id == gouvernement_type_id).first()
    if not db_gouvernement_type:
        raise Exception("GouvernementType not found")
    gouvernement_type_data = gouvernement_type.dict(exclude_unset=True)
    for key, value in gouvernement_type_data.items():
        setattr(db_gouvernement_type, key, value)
    db.add(db_gouvernement_type)
    db.commit()
    db.refresh(db_gouvernement_type)
    return db_gouvernement_type


def delete_gouvernement_types(db: Session, gouvernement_type_id: int):
    db_gouvernement_type = db.query(models.GouvernementType).filter(models.GouvernementType.id == gouvernement_type_id).first()
    if not db_gouvernement_type:
        raise Exception("GouvernementType not found")
    db.delete(db_gouvernement_type)
    db.commit()
    return db_gouvernement_type


# Gouvernement

def get_gouvernements(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Gouvernement).offset(skip).limit(limit).all()


def create_gouvernement(db: Session, gouvernement: schemas.GouvernementCreate):
    db_item = models.Gouvernement(**gouvernement.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_gouvernement(db: Session, gouvernement_id: int, gouvernement: schemas.GouvernementUpdate):
    db_gouvernement = db.query(models.Gouvernement).filter(models.Gouvernement.id == gouvernement_id).first()
    if not db_gouvernement:
        raise Exception("Gouvernement not found")
    gouvernement_data = gouvernement.dict(exclude_unset=True)
    for key, value in gouvernement_data.items():
        setattr(db_gouvernement, key, value)
    db.add(db_gouvernement)
    db.commit()
    db.refresh(db_gouvernement)
    return db_gouvernement


def delete_gouvernement(db: Session, gouvernement_id: int):
    db_gouvernement = db.query(models.Gouvernement).filter(models.Gouvernement.id == gouvernement_id).first()
    if not db_gouvernement:
        raise Exception("Gouvernement not found")
    db.delete(db_gouvernement)
    db.commit()
    return db_gouvernement


# Location

def get_locations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Location).offset(skip).limit(limit).all()


def create_location(db: Session, location: schemas.LocationCreate):
    db_item = models.Location(**location.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_location(db: Session, location_id: int, location: schemas.LocationUpdate):
    db_location = db.query(models.Location).filter(models.Location.id == location_id).first()
    if not db_location:
        raise Exception("Location not found")
    location_data = location.dict(exclude_unset=True)
    for key, value in location_data.items():
        setattr(db_location, key, value)
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location


def delete_location(db: Session, location_id: int):
    db_location = db.query(models.Location).filter(models.Location.id == location_id).first()
    if not db_location:
        raise Exception("Location not found")
    db.delete(db_location)
    db.commit()
    return db_location
