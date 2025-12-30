from fastapi import APIRouter, Depends
from ..deps import get_current_user
from .service import run_agent

router = APIRouter(prefix="/chat", tags=["AI"])

@router.post("")
def chat(prompt: str, user=Depends(get_current_user)):
    return {"response": run_agent(user, prompt)}
