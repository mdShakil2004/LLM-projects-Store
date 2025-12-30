import stripe
from ..config import settings

stripe.api_key = settings.STRIPE_SECRET

def create_checkout(price_id, success, cancel):
    return stripe.checkout.Session.create(
        mode="subscription",
        line_items=[{"price": price_id, "quantity": 1}],
        success_url=success,
        cancel_url=cancel,
    )
