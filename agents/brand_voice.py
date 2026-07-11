# agents/brand_voice.py
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from templates.brand_personas import BRAND_PERSONAS, PLATFORM_TEMPLATES
from dotenv import load_dotenv

load_dotenv()

def generate_marketing_copy(
    brief: str,
    platform: str = "instagram",
    persona: str = "witty"
) -> dict:
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.7,
    )

    system_prompt = BRAND_PERSONAS.get(
        persona,
        BRAND_PERSONAS["witty"]
    )

    platform_template = PLATFORM_TEMPLATES.get(
        platform,
        PLATFORM_TEMPLATES["instagram"]
    )

    user_prompt = platform_template.format(
        brief=brief,
        persona=persona.upper()
    )

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ]

    response = llm.invoke(messages)

    return {
        "brief": brief,
        "platform": platform,
        "persona": persona,
        "copy": response.content
    }