from app.users.repository import get_user_by_email,create_user
from app.core.security import hash_password,verify_password,create_access_token
from fastapi import HTTPException

def register(db,name,password,email):
    if get_user_by_email(db,email):
        raise Exception("already register")
    
    user=create_user(db,name,hash_password(password),email)
    return user

def loginuser(db,email,password):
    user=get_user_by_email(db,email)
    if not user:
        raise HTTPException(
        status_code=401,
        detail="Invalid credentials")
    
    if not verify_password(password,user.password) :
        raise HTTPException(
        status_code=401,
        detail="Invalid credentials")
    
    token=create_access_token({"sub":user.email})

    return {
    "access_token": token,
    "token_type": "bearer"
    }