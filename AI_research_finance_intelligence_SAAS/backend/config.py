import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME = "AI SaaS Platform"
    JWT_SECRET = os.getenv("JWT_SECRET", "dev-secret")
    JWT_ALGO = "HS256"
    ACCESS_EXPIRE_MIN = 30
    REFRESH_EXPIRE_DAYS = 7

    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")

    STRIPE_SECRET = os.getenv("STRIPE_SECRET", "")
    STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET", "")

    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

settings = Settings()
