from .auth import users

def get_user_profile(username: str):
    if username not in users:
        raise Exception("User not found")
    return {"username": username}
