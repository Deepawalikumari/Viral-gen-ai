# workers/image_worker.py
from celery_app import celery_app
from agents.prompt_enhancer import enhance_prompt
from agents.brand_voice import generate_marketing_copy
from core.stable_diffusion import generate_image
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
        self.update_state(
            state="PROGRESS",
            meta={"status": "Enhancing prompt..."}
        )
        enhanced_prompt = enhance_prompt(brief)

        self.update_state(
            state="PROGRESS",
            meta={"status": "Generating copy..."}
        )
        copy_result = generate_marketing_copy(
            brief, platform, persona
        )

        self.update_state(
            state="PROGRESS",
            meta={"status": "Generating image..."}
        )
        image_path = generate_image(enhanced_prompt)

        return {
            "status": "completed",
            "job_id": job_id,
            "brief": brief,
            "platform": platform,
            "persona": persona,
            "enhanced_prompt": enhanced_prompt,
            "copy": copy_result["copy"],
            "image_path": image_path,
            "image_url": f"http://localhost:8000/{image_path}"
        }

    except Exception as e:
        return {
            "status": "failed",
            "error": str(e)
        }