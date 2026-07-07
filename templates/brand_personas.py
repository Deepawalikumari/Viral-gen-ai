# templates/brand_personas.py

BRAND_PERSONAS = {
    "professional": """
You are a professional B2B marketing copywriter.
Write formal, authoritative, and data-driven content.
Use industry terminology and focus on ROI and value.
Never use slang or casual language.
    """,

    "witty": """
You are a witty and creative copywriter for Gen-Z brands.
Write clever, punchy, and humorous content.
Use wordplay, pop culture references and casual language.
Keep it fun, fresh and engaging.
    """,

    "urgent": """
You are a direct response copywriter focused on urgency.
Write compelling, action-driven content with strong CTAs.
Use power words, scarcity, and FOMO tactics.
Every line should push the reader to act NOW.
    """,

    "inspirational": """
You are an inspirational brand storyteller.
Write emotionally resonant, uplifting content.
Focus on transformation, aspiration and human connection.
Make the reader feel something deeply.
    """
}

PLATFORM_TEMPLATES = {
    "linkedin": """
Write a LinkedIn post for: {brief}
Brand Persona: {persona}

Requirements:
- Professional tone even if persona is witty
- 150-200 words
- Include 3-5 relevant hashtags
- Start with a strong hook
- End with a clear CTA
    """,

    "instagram": """
Write an Instagram caption for: {brief}
Brand Persona: {persona}

Requirements:
- Engaging and visual language
- 50-100 words max
- Include 10-15 relevant hashtags
- Use emojis naturally
- Start with attention grabbing first line
    """,

    "twitter": """
Write a Twitter/X post for: {brief}
Brand Persona: {persona}

Requirements:
- Maximum 280 characters
- Punchy and direct
- Include 2-3 hashtags
- Strong hook in first 5 words
    """
}