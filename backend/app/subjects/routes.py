from fastapi import APIRouter,Depends
from app.database.session import get_db
from sqlalchemy.orm import Session
from .service import list_subject,get_subject

router = APIRouter(
    prefix="/subjects",
    tags=["Subjects"]
)

@router.get("/")
def get_subjects(db:Session=Depends(get_db)):
    return list_subject(db)

@router.get("/{id}")
def get_subject_by_id(id:int,db:Session=Depends(get_db)):
    return get_subject(db,id)
