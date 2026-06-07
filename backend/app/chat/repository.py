from sqlalchemy.orm import Session
from app.models.chat_msg import ChatMessage

def create_chat_message(
    db: Session,
    user_id: int,
    message: str,
    response: str
):
    chat = ChatMessage(
        user_id=user_id,
        message=message,
        response=response
    )

    db.add(chat)
    db.commit()
    db.refresh(chat)

    return chat


def get_chat_history(
    db: Session,
    user_id: int
):
    return (
        db.query(ChatMessage)
        .filter(
            ChatMessage.user_id == user_id
        )
        .all()
    )