# workers/image_worker.py
from celery_app import celery_app
from agents.prompt_enhancer import enhance_prompt
from agents.brand_voice import generate_marketing_copy
from core.stable_diffusion import generate_image
from core.database import update_job, save_to_history
import uuid

@celery_app.task(bind=True)
def generate_content_task(
    self,
    job_id: str,
    brief: str,
    platform: str,
    persona: str
):
    try:
        # Update status in MongoDB
        update_job(job_id, {"status": "processing"})

        self.update_state(
            state="PROGRESS",
            meta={"status": "Enhancing prompt..."}
        )

        # Step 1 — Enhance prompt
        enhanced_prompt = enhance_prompt(brief)
        update_job(job_id, {
            "enhanced_prompt": enhanced_prompt
        })

        self.update_state(
            state="PROGRESS",
            meta={"status": "Generating copy..."}
        )

        # Step 2 — Generate copy
        copy_result = generate_marketing_copy(
            brief, platform, persona
        )
        update_job(job_id, {
            "copy": copy_result["copy"]
        })

        self.update_state(
            state="PROGRESS",
            meta={"status": "Generating image..."}
        )

        # Step 3 — Generate image
        image_path = generate_image(enhanced_prompt)
        image_url = f"http://localhost:8000/{image_path}"

        # Final result
        result = {
            "status": "completed",
            "job_id": job_id,
            "brief": brief,
            "platform": platform,
            "persona": persona,
            "enhanced_prompt": enhanced_prompt,
            "copy": copy_result["copy"],
            "image_path": image_path,
            "image_url": image_url
        }

        # Update MongoDB
        update_job(job_id, result)

        # Save to history
        save_to_history(result)

        return result

    except Exception as e:
        update_job(job_id, {
            "status": "failed",
            "error": str(e)
        })
        return {
            "status": "failed",
            "error": str(e)
        }