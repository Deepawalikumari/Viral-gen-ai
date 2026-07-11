# test_week3.py
import requests
import time

BASE_URL = "http://localhost:8000"

print("=" * 50)
print("WEEK 3 TEST — ASYNC QUEUE SYSTEM")
print("=" * 50)

# ── TEST 1: Submit single job ─────────────────────
print("\n📤 TEST 1: Submit single job...")
response = requests.post(
    f"{BASE_URL}/generate",
    json={
        "brief": "red running shoes for athletes",
        "platform": "instagram",
        "persona": "witty"
    }
)
data = response.json()
print(f"✅ Job ID: {data['job_id']}")
print(f"✅ Task ID: {data['task_id']}")
print(f"✅ Status: {data['status']}")

task_id = data['task_id']

# ── TEST 2: Poll for result ───────────────────────
print("\n📊 TEST 2: Polling for result...")
while True:
    response = requests.get(
        f"{BASE_URL}/job/{task_id}"
    )
    data = response.json()
    status = data["status"]
    print(f"Status: {status}")

    if status == "completed":
        print(f"✅ Copy: {data['result']['copy'][:100]}...")
        print(f"✅ Image: {data['result']['image_url']}")
        break
    elif status == "failed":
        print(f"❌ Error: {data}")
        break

    time.sleep(2)

# ── TEST 3: Submit 5 concurrent jobs ─────────────
print("\n📤 TEST 3: Submit 5 concurrent jobs...")
briefs = [
    "red running shoes",
    "coffee shop interior",
    "luxury watch",
    "sports car",
    "mountain landscape"
]

task_ids = []
for brief in briefs:
    response = requests.post(
        f"{BASE_URL}/generate",
        json={
            "brief": brief,
            "platform": "instagram",
            "persona": "witty"
        }
    )
    data = response.json()
    task_ids.append(data["task_id"])
    print(f"✅ Submitted: {brief}")

# ── TEST 4: Check server responsive ──────────────
print("\n🔍 TEST 4: Server responsiveness...")
for i in range(3):
    start = time.time()
    response = requests.get(f"{BASE_URL}/")
    end = time.time()
    ms = round((end - start) * 1000)
    print(f"Response time: {ms}ms ✅")

# ── TEST 5: Poll all 5 jobs ───────────────────────
print("\n📊 TEST 5: Polling all 5 jobs...")
completed = []
failed = []

while len(completed) + len(failed) < len(task_ids):
    for task_id in task_ids:
        if task_id in completed or task_id in failed:
            continue

        response = requests.get(
            f"{BASE_URL}/job/{task_id}"
        )
        data = response.json()
        status = data["status"]

        if status == "completed":
            completed.append(task_id)
            print(f"✅ Job {task_id[:8]} completed!")
        elif status == "failed":
            failed.append(task_id)
            print(f"❌ Job {task_id[:8]} failed!")
        else:
            print(f"⏳ Job {task_id[:8]}: {status}")

    time.sleep(2)

print(f"\n✅ Completed: {len(completed)}/5")
print(f"❌ Failed: {len(failed)}/5")

print("\n" + "=" * 50)
print("WEEK 3 COMPLETE ✅")
print("=" * 50)