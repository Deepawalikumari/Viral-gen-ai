# routers/generate.py
from fastapi import APIRouter
from pydantic import BaseModel
from workers.image_worker import generate_content_task
import uuid

router = APIRouter()

class GenerateRequest(BaseModel):
    brief: str
    platform: str = "instagram"
    persona: str = "witty"

@router.post("/generate")
async def generate(request: GenerateRequest):
    """
    Submit generation job.
    Returns Job ID immediately! ✅
    """
    job_id = str(uuid.uuid4())

    # Send to Celery worker
    task = generate_content_task.delay(
        job_id=job_id,
        brief=request.brief,
        platform=request.platform,
        persona=request.persona
    )

    return {
        "job_id": job_id,
        "task_id": task.id,
        "status": "pending",
        "message": f"Job submitted! Poll /job/{task.id} for status"
    }