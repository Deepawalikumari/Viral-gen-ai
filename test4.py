# test_week4.py
import requests
import time

BASE_URL = "http://localhost:8000"

print("=" * 50)
print("WEEK 4 TEST — INTEGRATION & PERSISTENCE")
print("=" * 50)

# TEST 1 — Submit job
print("\n📤 TEST 1: Submit job...")
response = requests.post(
    f"{BASE_URL}/generate",
    json={
        "brief": "luxury coffee brand",
        "platform": "instagram",
        "persona": "professional"
    }
)
data = response.json()
task_id = data["task_id"]
print(f"✅ Job submitted: {task_id[:8]}...")

# TEST 2 — Poll until complete
print("\n📊 TEST 2: Polling...")
while True:
    response = requests.get(f"{BASE_URL}/job/{task_id}")
    data = response.json()
    print(f"Status: {data['status']}")

    if data["status"] == "completed":
        result = data["result"]
        print(f"✅ Copy: {result['copy'][:80]}...")
        print(f"✅ Image: {result['image_url']}")
        print(f"✅ Prompt: {result['enhanced_prompt'][:80]}...")
        break
    elif data["status"] == "failed":
        print(f"❌ Error: {data}")
        break

    time.sleep(2)

# TEST 3 — Check history
print("\n📚 TEST 3: Check history...")
response = requests.get(f"{BASE_URL}/history")
data = response.json()
print(f"✅ History count: {data['count']}")
for item in data["history"][:3]:
    print(f"  - {item['brief']} ({item['platform']})")

print("\n" + "=" * 50)
print("WEEK 4 COMPLETE ✅")
print("=" * 50)