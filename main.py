# main.py - ViralGen AI
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import generate, jobs
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="ViralGen AI 🎨")

# Serve static files
os.makedirs("static/outputs", exist_ok=True)
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

# Include routers
app.include_router(generate.router)
app.include_router(jobs.router)

@app.get("/")
def home():
    return {
        "message": "ViralGen AI is running! 🎨",
        "endpoints": {
            "generate": "POST /generate",
            "job_status": "GET /job/{task_id}"
        }
    }