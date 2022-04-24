from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
import crud

from routers import users, characteres, influences, powers, gouvernement_types, gouvernements, locations


from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

app.include_router(users.router)
app.include_router(characteres.router)
app.include_router(influences.router)
app.include_router(powers.router)
app.include_router(gouvernement_types.router)
app.include_router(gouvernements.router)
app.include_router(locations.router)



