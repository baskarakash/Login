# jwt_handler.py

import time
import jwt
from decouple import config
from fastapi import HTTPException
from passlib.context import CryptContext

MIN_TOKEN_LENGTH = 50

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

# Password hashing context
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class PasswordHashing:
    @staticmethod
    def hash_password(password: str) -> str:
        return password_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return password_context.verify(plain_password, hashed_password)

def is_valid_token_format(token_value: str) -> bool:
    return token_value.isalnum()

def token_response(token: str):
    return {
        "access_token": token
    }

def signJWT(userID: str):
    payload = {
        "userID": userID,
        "expiry": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    if len(token) < MIN_TOKEN_LENGTH:
        raise HTTPException(status_code=500, detail="Token generation failed")

    return token_response(token)

def decodeJWT(token: str):
    try:
        if not token.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Invalid token format")

        token_value = token[len("Bearer "):].strip()

        if len(token_value) < MIN_TOKEN_LENGTH:
            raise HTTPException(status_code=401, detail="Invalid token length")

        if not is_valid_token_format(token_value):
            raise HTTPException(status_code=401, detail="Invalid token format")

        decode_token = jwt.decode(token_value, JWT_SECRET, algorithms=[JWT_ALGORITHM])

        user_id = decode_token.get('userID')
        expiry = decode_token.get('expiry')

        if not user_id or not expiry or expiry < time.time():
            raise HTTPException(status_code=401, detail="Invalid token")

        return decode_token
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired. Please log in again.")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token. Please provide a valid access token.")
    except Exception as e:
        print(f"Error decoding token: {e}")
        raise HTTPException(status_code=401, detail=f"Error decoding token: {e}. Please try again.")
