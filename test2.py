# test_week2.py
from agents.prompt_enhancer import enhance_prompt
from core.stable_diffusion import generate_image
import os

print("=" * 50)
print("WEEK 2 TEST — IMAGE GENERATION")
print("=" * 50)

brief = "red running shoes for athletes"

# TEST 1 — Prompt Enhancement
print("\n🔮 TEST 1: Prompt Enhancement...")
enhanced = enhance_prompt(brief)
print(f"Original: {brief}")
print(f"Enhanced: {enhanced}")

# TEST 2 — Image Generation
print("\n🎨 TEST 2: Image Generation...")
image_path = generate_image(enhanced)
print(f"✅ Image saved at: {image_path}")

# TEST 3 — Consistency test
print("\n🔄 TEST 3: Consistency Test...")
for i in range(3):
    path = generate_image(enhanced)
    print(f"Image {i+1}: {path}")

print("\n" + "=" * 50)
print("WEEK 2 COMPLETE ✅")
print("=" * 50)