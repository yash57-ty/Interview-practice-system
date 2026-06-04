from app.subjects.repository import get_all_subjects,get_subject_by_id

def list_subject(db):
    return get_all_subjects(db)

def get_subject(db,id:int):
    return get_subject_by_id(db,id)
