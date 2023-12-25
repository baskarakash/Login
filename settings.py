# settings.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

MIN_TOKEN_LENGTH = 50

# Your other settings...
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# Database Configuration
DATABASE_URL = "postgresql://postgres:root@db:5432/login"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
