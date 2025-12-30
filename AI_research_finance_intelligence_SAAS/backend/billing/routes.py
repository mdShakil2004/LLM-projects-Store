from fastapi import APIRouter
from .stripe import create_checkout

router = APIRouter(prefix="/billing")

@router.post("/checkout")
def checkout(price_id: str):
    session = create_checkout(
        price_id,
        "https://yourapp.com/success",
        "https://yourapp.com/cancel"
    )
    return {"url": session.url}
