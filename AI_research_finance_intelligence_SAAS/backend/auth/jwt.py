from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from ..config import settings

pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def hash_password(p: str):
    return pwd.hash(p)

def verify_password(p, h):
    return pwd.verify(p, h)

def create_token(data: dict, expires: int):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(minutes=expires)
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGO)

def decode_token(token: str = Depends(oauth2_scheme)):
    try:
        return jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGO])
    except JWTError:
        raise HTTPException(401, "Invalid token")
