from fastapi import FastAPI
from .auth import signup_user, login_user, UserSignup, UserLogin
from .calculator import add, subtract, multiply, divide, power
from .order_service import create_order
from .user_service import get_user_profile

app = FastAPI()

@app.post("/signup")
def signup(user: UserSignup):
    return signup_user(user)

@app.post("/login")
def login(user: UserLogin):
    return login_user(user)

@app.get("/calc/add")
def calc_add(a: float, b: float):
    return {"result": add(a, b)}

@app.get("/order")
def order(item: str, qty: int, username: str):
    return create_order(item, qty, username)

@app.get("/user/profile")
def get_profile(username: str):
    return get_user_profile(username)
