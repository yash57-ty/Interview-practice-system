from sqlalchemy import Column,Integer,String,ForeignKey
from app.database.base import Base

class Roadmap(Base):

    __tablename__="roadmaps"

    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )
    subject_id=Column(
        Integer,
        ForeignKey("subjects.id"),
        nullable=False
    )
    week=Column(
        Integer,
        nullable=False
    )
    title=Column(
        String,
        nullable=False
    )
    description=Column(
        String,
        nullable=False
    )