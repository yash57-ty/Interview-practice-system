from fastapi import FastAPI
from app.auth.routes import router as auth
from app.subjects.routes import router as subject
from app.progress.routes import router as progress
from app.topics.routes import router as topic_router
from app.roadmap.routes import router as roadmap_router
from app.chat.routes import router as chat_router
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(roadmap_router)
app.include_router(auth)
app.include_router(subject)
app.include_router(progress)
app.include_router(topic_router)
app.include_router(chat_router)
@app.get("/")
def home():
    return {"message":"backend running"}