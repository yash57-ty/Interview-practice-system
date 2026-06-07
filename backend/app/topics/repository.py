from app.models.topics import Topic
from sqlalchemy.orm import Session


def get_all_topics(db:Session):
    return db.query(Topic).all()

def get_all_topics_id(db:Session,topic_id:int):
    return db.query(Topic).filter(Topic.id==topic_id).first()

def get_all_topics_by_subject(db:Session,subject_id:int):    
    return db.query(Topic).filter(Topic.subject_id==subject_id).all()
