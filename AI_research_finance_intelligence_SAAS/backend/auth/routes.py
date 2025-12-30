from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import User
from .jwt import hash_password, verify_password, create_token
from ..config import settings

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(email: str, password: str):
    db = SessionLocal()
    user = User(email=email, password=hash_password(password))
    db.add(user)
    db.commit()
    return {"message": "registered"}

@router.post("/login")
def login(email: str, password: str):
    db = SessionLocal()
    user = db.query(User).filter(User.email == email).first()

    if not user or not verify_password(password, user.password):
        return {"error": "invalid credentials"}

    access = create_token({"sub": user.email}, settings.ACCESS_EXPIRE_MIN)
    refresh = create_token({"sub": user.email}, settings.REFRESH_EXPIRE_DAYS * 1440)

    return {
        "access_token": access,
        "refresh_token": refresh,
        "plan": user.plan
    }
