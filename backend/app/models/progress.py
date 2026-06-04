from sqlalchemy import Column, Integer, ForeignKey
from app.database.base import Base


class Progress(Base):

    __tablename__ = "progress"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )
    subject_id = Column(
        Integer,
        ForeignKey("subjects.id"),
        nullable=False
    )
    completed_topics = Column(
        Integer,
        nullable=False
    )
    total_topics = Column(
        Integer,
        nullable=False
    )
    percentage = Column(
        Integer,
        nullable=False
    )