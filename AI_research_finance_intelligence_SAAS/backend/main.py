from fastapi import FastAPI
from .database import Base, engine
from .auth.routes import router as auth_router
from .agents.runner import router as chat_router
from .billing.routes import router as billing_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI SaaS Platform")

app.include_router(auth_router)
app.include_router(chat_router)
app.include_router(billing_router)

@app.get("/")
def root():
    return {"status": "running"}
