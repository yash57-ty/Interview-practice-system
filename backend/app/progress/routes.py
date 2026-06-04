from .schemas import ProgressCreate
from fastapi import APIRouter,Depends
from app.core.dependencies import get_current_user
from .service import get_user_progress,create_user_progress
from sqlalchemy.orm import Session
from app.core.dependencies import get_db


router = APIRouter(
    prefix="/progress",
    tags=["Progress"]
)


@router.post("/")
def save_progress(
    progress: ProgressCreate,db: Session = Depends(get_db),
    current_user=Depends(get_current_user)):
    return create_user_progress(
        db,
        progress,
        current_user
    )

@router.get("/")
def get_progress(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return get_user_progress(
        db,
        current_user
    )