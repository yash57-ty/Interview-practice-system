from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.core.dependencies import get_current_user

from app.roadmap.schemas import RoadmapCreate
from app.roadmap.service import (
    generate_roadmap,
    get_my_roadmaps
)
from .repository import get_user_subject_roadmaps

router = APIRouter(
    prefix="/roadmaps",
    tags=["Roadmaps"]
)

@router.post("/generate")
def create_user_roadmap(
    roadmap: RoadmapCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return generate_roadmap(
        db,
        roadmap,
        current_user
    )

@router.get("/")
def get_roadmaps(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return get_my_roadmaps(
        db,
        current_user
    )

@router.get("/{subject_id}")
def get_subject_roadmap(
    subject_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return get_user_subject_roadmaps(
        db,
        current_user.id,
        subject_id
    )