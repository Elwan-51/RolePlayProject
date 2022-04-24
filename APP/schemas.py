from typing import List, Optional

from pydantic import BaseModel


# Characteres

class CharacteresBase(BaseModel):
    name: str
    description: Optional[str] = None
    influence_id: Optional[int] = None
    power_id: Optional[int] = None


class CharacteresCreate(CharacteresBase):
    pass


class Characteres(CharacteresBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class CharacteresUpdate(CharacteresBase):
    name: Optional[str] = None


# User

class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Characteres] = []

    class Config:
        orm_mode = True


class UserUpdate(UserBase):
    username: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None


# Location

class LocationBase(BaseModel):
    name: str
    description: Optional[str] = None
    influence_id: Optional[int] = None
    gouvernement_id: Optional[int] = None


class LocationCreate(LocationBase):
    pass


class Location(LocationBase):
    id: int

    class Config:
        orm_mode = True


class LocationUpdate(LocationBase):
    name: Optional[str] = None


# Gouvernement

class GouvernementBase(BaseModel):
    name: str
    description: Optional[str] = None
    gouvernement_type_id: int
    influence_id: Optional[int] = None


class GouvernementCreate(GouvernementBase):
    pass


class Gouvernement(GouvernementBase):
    id: int
    locations: List[Location] = []

    class Config:
        orm_mode = True


class GouvernementUpdate(GouvernementBase):
    name: Optional[str] = None
    gouvernement_type_id: Optional[int] = None


# Influences

class InfluencesBase(BaseModel):
    name: str
    description: Optional[str] = None


class InfluencesCreate(InfluencesBase):
    pass


class Influences(InfluencesBase):
    id: int
    characteres: List[Characteres] = []
    gouvernements: List[Gouvernement] = []
    locations: List[Location] = []

    class Config:
        orm_mode = True


class InfluencesUpdate(InfluencesBase):
    name: Optional[str] = None


# Powers

class PowersBase(BaseModel):
    name: str
    description: Optional[str] = None


class PowersCreate(PowersBase):
    pass


class Powers(PowersBase):
    id: int
    characteres: List[Characteres] = []

    class Config:
        orm_mode = True


class PowersUpdate(PowersBase):
    name: Optional[str] = None


# GouvernementTypes

class GouvernementTypesBase(BaseModel):
    name: str
    description: Optional[str] = None


class GouvernementTypesCreate(GouvernementTypesBase):
    pass


class GouvernementTypes(GouvernementTypesBase):
    id: int
    gouvernements: List[Gouvernement] = []

    class Config:
        orm_mode = True


class GouvernementTypesUpdate(GouvernementTypesBase):
    name: Optional[str] = None






