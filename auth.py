from fastapi import HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)

users = {}

class UserSignup(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

def signup_user(user: UserSignup):
    if user.username in users:
        raise HTTPException(status_code=400, detail="User already exists")

    users[user.username] = pwd_context.hash(user.password)
    return {"message": "User created successfully"}

def login_user(user: UserLogin):
    if user.username not in users:
        raise HTTPException(status_code=404, detail="User not found")

    hashed_password = users[user.username]
    if not pwd_context.verify(user.password, hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": "Login successful"}
