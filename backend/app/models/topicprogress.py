from sqlalchemy import Column, Integer, Boolean, ForeignKey
from app.database.base import Base


class UserTopicProgress(Base):

    __tablename__ = "user_topic_progress"
    id = Column(
        Integer,
        primary_key=True,
        index=True
    )
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )
    topic_id = Column(
        Integer,
        ForeignKey("topics.id"),
        nullable=False
    )
    is_completed = Column(
        Boolean,
        default=False,
        nullable=False
    )