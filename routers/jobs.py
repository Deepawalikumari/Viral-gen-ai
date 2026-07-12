# routers/jobs.py
from fastapi import APIRouter
from celery_app import celery_app
from celery.result import AsyncResult
from core.database import get_history

router = APIRouter()

@router.get("/job/{task_id}")
async def get_job_status(task_id: str):
    """Poll this endpoint to check job status."""
    task = AsyncResult(task_id, app=celery_app)

    if task.state == "PENDING":
        return {
            "task_id": task_id,
            "status": "pending",
            "message": "Job waiting to start..."
        }

    elif task.state == "PROGRESS":
        return {
            "task_id": task_id,
            "status": "processing",
            "message": task.info.get("status", "Processing...")
        }

    elif task.state == "SUCCESS":
        return {
            "task_id": task_id,
            "status": "completed",
            "result": task.result
        }

    elif task.state == "FAILURE":
        return {
            "task_id": task_id,
            "status": "failed",
            "error": str(task.result)
        }

    return {"task_id": task_id, "status": task.state}

@router.get("/history")
async def get_history_endpoint():
    """Get recent generation history."""
    history = get_history(limit=10)
    return {
        "count": len(history),
        "history": history
    }