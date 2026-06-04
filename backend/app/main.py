from fastapi import FastAPI
from app.auth.routes import router as auth
from app.subjects.routes import router as subject
from app.progress.routes import router as progress
app=FastAPI()

app.include_router(auth)
app.include_router(subject)
app.include_router(progress)
@app.get("/")
def home():
    return {"message":"backend running"}