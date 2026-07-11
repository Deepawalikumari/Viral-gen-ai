
# core/stable_diffusion.py
import requests
import uuid
import os
from urllib.parse import quote

OUTPUT_DIR = "static/outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_image(prompt: str) -> str:
    """
    Generate image using Pollinations AI.
    No API key needed! Free!
    """
    print(f"🎨 Generating image...")
    print(f"Prompt: {prompt[:80]}...")

    # Encode prompt for URL
    encoded_prompt = quote(prompt)

    # Pollinations AI URL
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"

    params = {
        "width": 512,
        "height": 512,
        "nologo": "true",
        "enhance": "true"
    }

    # Download image
    response = requests.get(
        url,
        params=params,
        timeout=120
    )

    if response.status_code != 200:
         print("Status Code:", response.status_code)
         print("Response:", response.text)
         raise Exception(f"API Error: {response.status_code}")

    # Save image
    filename = f"{uuid.uuid4().hex}.png"
    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, "wb") as f:
        f.write(response.content)

    print(f"✅ Image saved: {filepath}")
    return filepath