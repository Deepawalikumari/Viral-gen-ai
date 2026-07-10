# agents/prompt_enhancer.py
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

ENHANCER_SYSTEM_PROMPT = """
You are an expert AI image prompt engineer.
Transform simple briefs into detailed image prompts.

Rules:
1. Add lighting details (cinematic, golden hour, studio)
2. Add quality tags (8k, photorealistic, highly detailed)
3. Add style (commercial photography, product shot)
4. Add composition (close-up, wide shot, centered)
5. Add background details
6. Keep under 150 words
7. Return ONLY the enhanced prompt, nothing else
No explanation, no preamble, just the prompt!
"""

def enhance_prompt(brief: str) -> str:
    """
    Transform simple brief into detailed image prompt.

    Example:
    Input:  "red shoes"
    Output: "photorealistic red running shoes on wet
             asphalt track, cinematic lighting, 8k
             resolution, commercial photography..."
    """
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.8,
    )

    messages = [
        SystemMessage(content=ENHANCER_SYSTEM_PROMPT),
        HumanMessage(
            content=f"Enhance this brief into an image prompt: {brief}"
        )
    ]

    response = llm.invoke(messages)
    return response.content