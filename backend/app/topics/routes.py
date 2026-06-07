from fastapi import Depends,APIRouter
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.topics.service import list_topics,get_topic,get_subject_topics

router=APIRouter(
    prefix="/topics",
    tags=["Topics"]
)

@router.get("/")
def get_topics(db:Session=Depends(get_db)):
    return list_topics(db)

@router.get("/{topic_id}")
def get_topic_by_id(
    topic_id: int,
    db: Session = Depends(get_db)
):
    return get_topic(db, topic_id)

@router.get("/subject/{subject_id}")
def get_topics_by_subject(
    subject_id: int,
    db: Session = Depends(get_db)
):
    return get_subject_topics(
        db,
        subject_id
    )