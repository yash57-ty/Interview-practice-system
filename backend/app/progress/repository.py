from app.models.progress import Progress
from sqlalchemy.orm import Session

def create_progress(
    db: Session,user_id: int,
    subject_id: int,completed_topics: int,
    total_topics: int,percentage: int):
    
    progress = Progress(
    user_id=user_id,
    subject_id=subject_id,
    completed_topics=completed_topics,
    total_topics=total_topics,
    percentage=percentage)

    db.add(progress)
    db.commit()
    db.refresh(progress)
    return progress

def get_progress_by_user(db:Session,user_id:int):
    return db.query(Progress).filter(Progress.user_id==user_id).all()
