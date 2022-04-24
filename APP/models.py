from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    characteres = relationship("Charactere", back_populates="owner_")


class Charactere(Base):
    __tablename__ = "characteres"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    influence_id = Column(Integer, ForeignKey("influences.id"))
    power_id = Column(Integer, ForeignKey("powers.id"), unique=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner_ = relationship("User", back_populates="characteres")
    influence_ = relationship("Influences", back_populates="characteres")
    power_ = relationship("Powers", back_populates="characteres")


class Influences(Base):
    __tablename__ = "influences"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)

    characteres = relationship("Charactere", back_populates="influence_")
    gouvernements = relationship("Gouvernement", back_populates="influence_")
    locations = relationship("Location", back_populates="influence_")


class Powers(Base):
    __tablename__ = "powers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, index=True)

    characteres = relationship("Charactere", back_populates="power_")


class GouvernementType(Base):
    __tablename__ = "gouvernement_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)

    gouvernements = relationship("Gouvernement", back_populates="gouvernement_type_")


class Gouvernement(Base):
    __tablename__ = "gouvernements"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    gouvernement_type_id = Column(Integer, ForeignKey("gouvernement_types.id"))
    influence_id = Column(Integer, ForeignKey("influences.id"))

    gouvernement_type_ = relationship("GouvernementType", back_populates="gouvernements")
    influence_ = relationship("Influences", back_populates="gouvernements")
    locations = relationship("Location", back_populates="gouvernement_")


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    influence_id = Column(Integer, ForeignKey("influences.id"))
    gouvernement_id = Column(Integer, ForeignKey("gouvernements.id"))

    influence_ = relationship("Influences", back_populates="locations")
    gouvernement_ = relationship("Gouvernement", back_populates="locations")

