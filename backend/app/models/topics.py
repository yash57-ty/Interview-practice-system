from sqlalchemy import Column, Integer, String,ForeignKey
from app.database.base import Base

class Topic(Base):
    __tablename__ = "topics"
    id=Column(Integer,primary_key=True,index=True)
    subject_id = Column(
        Integer,
        ForeignKey("subjects.id"),
        nullable=False
    )
    name=Column(String,nullable=False)
    description=Column(String,nullable=False)
    