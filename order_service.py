from .user_service import get_user_profile

orders = []

def create_order(item: str, qty: int, username: str):
    user = get_user_profile(username)
    order = {"user": username, "item": item, "qty": qty}
    orders.append(order)
    return {"message": "Order created", "order": order}
