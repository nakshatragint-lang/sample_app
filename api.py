
from fastapi import FastAPI
from .auth import signup_user, login_user, UserSignup, UserLogin
from .calculator import add, subtract, multiply, divide, power
from .order_service import create_order
from .user_service import get_user_profile
from .math_exp import factorial, fibonacci
from .string_utils import reverse_string, is_palindrome, count_words

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

@app.get("/calc/subtract")
def calc_subtract(a: float, b: float):          
    return {"result": subtract(a, b)}

@app.get("/calc/multiply")
def calc_multiply(a: float, b: float):
    return {"result": multiply(a, b)}

@app.get("/calc/divide")
def calc_divide(a: float, b: float):
    return {"result": divide(a, b)}

@app.get("/calc/power")
def calc_power(a: float, b: float):
    return {"result": power(a, b)}

@app.get("/calc/factorial")
def calc_factorial(n: int):
    return {"result": factorial(n)}

@app.get("/calc/fibonacci")
def calc_fibonacci(n: int):
    return {"result": fibonacci(n)}

@app.get("/string/reverse")
def string_reverse(s: str):
    return {"result": reverse_string(s)}    

@app.get("/string/is_palindrome")
def string_is_palindrome(text: str):
    return {"result": is_palindrome(text)}

@app.get("/string/count_words")
def string_count_words(sentence: str):
    return {"result": count_words(sentence)}

@app.get("/order")
def order(item: str, qty: int, username: str):
    return create_order(item, qty, username)

@app.get("/user/profile")
def get_profile(username: str):
    return get_user_profile(username)
