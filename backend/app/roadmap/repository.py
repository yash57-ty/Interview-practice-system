from sqlalchemy.orm import Session
from app.models.roadmap import Roadmap

def create_roadmap(db:Session,user_id:int,subject_id:int,week:int,title:str,description:str):
    roadmap = Roadmap(
        user_id=user_id,
        subject_id=subject_id,
        week=week,
        title=title,
        description=description
    )

    db.add(roadmap)
    db.commit()
    db.refresh(roadmap)

    return roadmap

def get_user_roadmaps(
    db: Session,
    user_id: int
):
    return (
        db.query(Roadmap)
        .filter(Roadmap.user_id == user_id)
        .all()
    )

def delete_user_roadmaps(
    db,
    user_id,
    subject_id
):
    db.query(Roadmap).filter(
        Roadmap.user_id == user_id,
        Roadmap.subject_id == subject_id
    ).delete()

    db.commit()

def get_user_subject_roadmaps(
    db,
    user_id,
    subject_id
):
    return db.query(Roadmap).filter(
        Roadmap.user_id == user_id,
        Roadmap.subject_id == subject_id
    ).all()