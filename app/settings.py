# settings.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from pydantic import(
    PostgresDsn
)
MIN_TOKEN_LENGTH = 50

load_dotenv()
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_SERVER = os.getenv("POSTGRES_SERVER")
POSTGRES_DB = os.getenv("POSTGRES_DB")
# POSTGRES_PORT =  os.getenv("")

# Your other settings...
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# Database Configuration
SQLALCHEMY_DATABASE_URI = PostgresDsn.build(scheme="postgresql", username=POSTGRES_USER,
                                            password=POSTGRES_PASSWORD, host=POSTGRES_SERVER,
                                            path=f"/{POSTGRES_DB or ''}")
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
