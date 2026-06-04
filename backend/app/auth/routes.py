from fastapi import APIRouter,Depends
from fastapi import Header
from fastapi import Request
from sqlalchemy.orm import Session
from app.database.session import get_db
from .schemas import UserRegister,UserLogin
from .service import register as userregister,loginuser
from app.core.security import verify_access_token
from app.core.dependencies import get_current_user,oauth2_scheme
from app.users.repository import get_user_by_email

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register")
def register(user:UserRegister,db:Session = Depends(get_db)):
    return userregister(db,name=user.name,password=user.password,email=user.email)

@router.post("/login")
def login(userlogin:UserLogin,db:Session=Depends(get_db)):
    print("hello")
    return loginuser(db,userlogin.name,userlogin.password)


@router.get("/me")
def get_me(
    current_user = Depends(get_current_user)
):
    return current_user

@router.get("/test")
async def test(request: Request):
    return dict(request.headers)

@router.get("/test2")
def test2(
    token: str = Depends(oauth2_scheme)
):
    return {"token": token}

@router.get("/test3")
def test3(
    token: str = Depends(oauth2_scheme)
):
    return {
        "email": verify_access_token(token)
    }

@router.get("/test4")
def test4(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    email = verify_access_token(token)

    user = get_user_by_email(
        db,
        email
    )

    return {
        "email": email,
        "user": str(user)
    }

