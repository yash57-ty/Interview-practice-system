from fastapi import APIRouter,Depends
from app.core.dependencies import get_current_user
from app.database.session import get_db
from sqlalchemy.orm import Session
from app.chat.schemas import ChatRequest
from .service import ask_gemini_and_save,get_user_chat_history

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.post("/")
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    
    return ask_gemini_and_save(
        db,
        current_user,
        request.message
    )

@router.get("/history")
def history(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return get_user_chat_history(
        db,
        current_user
    )