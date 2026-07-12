# core/database.py
from pymongo import MongoClient
from datetime import datetime
import uuid
import os
from dotenv import load_dotenv

load_dotenv()

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["viralgen"]
jobs_collection = db["jobs"]
history_collection = db["history"]

def create_job(
    brief: str,
    platform: str,
    persona: str
) -> str:
    """Create new job in MongoDB"""
    job_id = str(uuid.uuid4())
    jobs_collection.insert_one({
        "job_id": job_id,
        "brief": brief,
        "platform": platform,
        "persona": persona,
        "status": "pending",
        "created_at": datetime.now()
    })
    return job_id

def update_job(job_id: str, data: dict):
    """Update job status in MongoDB"""
    jobs_collection.update_one(
        {"job_id": job_id},
        {"$set": {**data, "updated_at": datetime.now()}}
    )

def get_job(job_id: str) -> dict:
    """Get job from MongoDB"""
    job = jobs_collection.find_one(
        {"job_id": job_id},
        {"_id": 0}
    )
    return job

def save_to_history(result: dict):
    """Save completed job to history"""
    history_collection.insert_one({
        **result,
        "saved_at": datetime.now()
    })

def get_history(limit: int = 10) -> list:
    """Get recent history"""
    history = list(
        history_collection.find(
            {},
            {"_id": 0}
        ).sort(
            "saved_at", -1
        ).limit(limit)
    )
    return history