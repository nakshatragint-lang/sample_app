from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext

app = FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

users = {}

class UserSignup(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str


@app.post("/signup")
def signup(user: UserSignup):
    if user.username in users:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_password = pwd_context.hash(user.password)
    users[user.username] = hashed_password

    return {"message": "User created successfully"}


@app.post("/login")
def login(user: UserLogin):
    if user.username not in users:
        raise HTTPException(status_code=404, detail="User not found")

    hashed_password = users[user.username]

    if not pwd_context.verify(user.password, hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": "Login successful"}
