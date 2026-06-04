from sqlalchemy.orm import Session

from app.models.subject import Subject

def get_all_subjects(db:Session):
    return db.query(Subject).all()

def get_subject_by_id(db:Session,subject_id:int):
    return db.query(Subject).filter(Subject.id==subject_id).first()