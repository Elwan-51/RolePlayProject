from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import yaml

with open('config.yaml', 'r') as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)


SQLALCHEMY_DATABASE_URL = f"postgresql://{cfg['Credential']['login']['username']}:{cfg['Credential']['login']['password']}@{cfg['Database']['url']}/{cfg['Database']['table']}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()