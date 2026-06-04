from pydantic import BaseModel


class ProgressCreate(BaseModel):
    subject_id:int
    completed_topics:int
    total_topics:int
    