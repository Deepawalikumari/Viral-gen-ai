# ViralGen AI 🎨
### Multi-Modal Social Media Content Generator

AI-powered tool that generates marketing copy
and images for social media campaigns.

## Features
- 🤖 AI Marketing Copy Generation
- 🎨 Image Generation (Stable Diffusion)
- 📱 Platform-specific content (LinkedIn, Instagram, Twitter)
- 🎭 Brand Voice Personas
- ⚡ Async Processing (Celery + Redis)
- 💾 History Logging (MongoDB)

## Tech Stack
| Tool | Purpose |
|---|---|
| FastAPI | Web framework |
| LangChain + Groq | AI text generation |
| Stable Diffusion | Image generation |
| Celery + Redis | Async task queue |
| MongoDB | Database |
| Pillow | Image compositing |

## Weekly Progress
- ⏳ Week 1 - Text Generation & Brand Personas
- ⏳ Week 2 - Image Generation Pipeline
- ⏳ Week 3 - Async Queue System
- ⏳ Week 4 - Integration & Persistence

---

## ⚙️ Setup & Installation

### Step 1 — Clone repository
```bash
git clone https://github.com/Deepawalikumari/Viral-gen-ai.git
cd Viral-gen-ai
```

### Step 2 — Create virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate
```

### Step 3 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Add API keys to `.env`
GROQ_API_KEY=your_groq_key_here

Get free Groq key at 👉 https://console.groq.com

### Step 5 — Start Redis (Memurai)

Memurai starts automatically as Windows service ✅
### Step 6 — Start Celery worker
```bash
celery -A celery_app worker --loglevel=info --pool=solo
```

### Step 7 — Start FastAPI server
```bash
uvicorn main:app --reload
```

### Step 8 — Open browser
http://localhost:8000

---

## 🚀 How to Use

### 1. Enter Brief
Type your marketing brief:
"red running shoes for athletes"
### 2. Select Platform
Instagram / LinkedIn / Twitter
### 3. Select Persona
Witty / Professional / Urgent / Inspirational
### 4. Generate
Click "Generate Content"
Get Job ID instantly ✅
Watch status updates live ✅
### 5. Get Results
📝 Marketing copy with hashtags
🎨 AI generated image
🔮 Enhanced prompt used

---

## 📅 Development Timeline

### Week 1 — Text Generation ✅
- Built brand persona system
- Created platform specific templates
- Tested all 4 personas × 3 platforms

### Week 2 — Image Generation ✅
- Built prompt enhancer agent
- Integrated Pollinations AI
- Tested image generation pipeline

### Week 3 — Async Queue ✅
- Integrated Celery + Redis
- Built job polling endpoint
- Load tested 5 concurrent jobs

### Week 4 — Integration & Persistence ✅
- Connected MongoDB for history
- Built complete web UI
- End to end testing complete

---

## 🧪 Testing

```bash
# Week 1 — Brand voice
python test1.py

# Week 2 — Image generation
python test2.py

# Week 3 — Async queue
python test3.py

# Week 4 — Full integration
python test4.py
```

---

## 📊 Sample Output

```json
{
  "status": "completed",
  "brief": "red running shoes",
  "platform": "instagram",
  "persona": "witty",
  "copy": "Sole mates found! 🏃 These red kicks
           will torch your competition...",
  "image_url": "http://localhost:8000/static/outputs/xxx.png",
  "enhanced_prompt": "Photorealistic red running shoes
                      on wet asphalt, cinematic lighting..."
}
```

---

## 🤝 Contributing

1. Fork the repository
2. Create branch (`git checkout -b feature/new-feature`)
3. Commit (`git commit -m "Add feature"`)
4. Push (`git push origin feature/new-feature`)
5. Open Pull Request

---

## 📝 License

MIT License

---

## 👩‍💻 Developer

**Deepali**
- GitHub: [@Deepawalikumari](https://github.com/Deepawalikumari)

---

## 🙏 Acknowledgements

- [LangChain](https://langchain.com) — AI framework
- [Groq](https://groq.com) — Free LLM API
- [Pollinations AI](https://pollinations.ai) — Free image generation
- [FastAPI](https://fastapi.tiangolo.com) — Web framework
- [Infotact Solutions](https://infotact.com) — Project guidance

---

⭐ **Star this repo if you found it helpful!**