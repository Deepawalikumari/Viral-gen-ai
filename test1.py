# test_week1.py
from agents.brand_voice import generate_marketing_copy

print("=" * 50)
print("WEEK 1 TEST — BRAND VOICE GENERATION")
print("=" * 50)

brief = "red running shoes for athletes"

# TEST 1 — All personas on Instagram
personas = ["professional", "witty", "urgent", "inspirational"]

for persona in personas:
    print(f"\n📝 Persona: {persona.upper()}")
    print("-" * 40)
    result = generate_marketing_copy(
        brief=brief,
        platform="instagram",
        persona=persona
    )
    print(result["copy"])
    print("-" * 40)

# TEST 2 — All platforms with witty persona
platforms = ["linkedin", "instagram", "twitter"]

for platform in platforms:
    print(f"\n📱 Platform: {platform.upper()}")
    print("-" * 40)
    result = generate_marketing_copy(
        brief=brief,
        platform=platform,
        persona="witty"
    )
    print(result["copy"])
    print("-" * 40)

print("\n" + "=" * 50)
print("WEEK 1 COMPLETE ✅")
print("=" * 50)