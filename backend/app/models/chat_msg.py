from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey
)
from app.database.base import Base


class ChatMessage(Base):
    __tablename__ = "chat_messages"
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
    message = Column(
        Text,
        nullable=False
    )
    response = Column(
        Text,
        nullable=False
    )