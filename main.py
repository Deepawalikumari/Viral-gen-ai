# main.py - ViralGen AI
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from routers import generate, jobs
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="ViralGen AI")

os.makedirs("static/outputs", exist_ok=True)

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

app.include_router(generate.router)
app.include_router(jobs.router)

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("static/index.html", encoding="utf-8") as f:
        return f.read()