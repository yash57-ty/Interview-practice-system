from sqlalchemy.orm import Session
from .repository import get_all_topics,get_all_topics_by_subject,get_all_topics_id

def list_topics(db:Session):
    return get_all_topics(db)

def get_topic(db:Session,topics_id:int):
    return get_all_topics_id(db,topics_id)

def get_subject_topics(db:Session,subject_id):
    return get_all_topics_by_subject(db,subject_id)
