
# 🚀 AI SaaS Platform – Multi-Agent Intelligence System

A production-ready **AI SaaS platform** built with a modular multi-agent architecture for research, finance intelligence, earnings analysis, and real-time insights.

This system combines **LLM agents, financial APIs, knowledge ingestion, authentication, billing, and usage tracking** into a scalable SaaS backend

---

Built by  <h1>Md Shakil</h1>
Focused on scalable systems, AI agents & production-grade architectures.


## ✨ Features

### 🧠 Multi-Agent Intelligence
- Planner / Orchestrator agent
- Finance analyst agent
- Earnings & transcript analyst
- Web, X (Twitter), Reddit, HackerNews researchers
- Fact-checking agent
- Thread / summary generator

### 📊 Finance & Earnings Intelligence
- Live market data (Polygon.io)
- Earnings calendar & transcripts
- Guidance & surprise analysis
- Company fundamentals
- Stock performance tracking

### 🔐 SaaS-Ready Architecture
- JWT authentication
- User accounts
- Subscription-ready billing (Stripe)
- Usage limits & credits
- Multi-tenant design
- Secure API access

### 🧠 Knowledge & Memory
- Upload PDFs & documents
- Persistent memory per user
- Knowledge-based reasoning
- Session storage with SQLite / PostgreSQL

### ⚙️ Engineering Highlights
- FastAPI backend
- Streamlit frontend
- Modular service architecture
- Agent orchestration (Agno)
- Background task support
- Clean separation of concerns
- Production-friendly structure

---
## output screen 
   <img width="1152" height="735" alt="image" src="https://github.com/user-attachments/assets/cb30ab62-d8aa-4299-bd29-81feb21386fb" />





##  diagram 
<img width="593" height="877" alt="image" src="https://github.com/user-attachments/assets/64712c6f-a423-473a-8c8e-761340559894" />

 

## env file required
```env
OPENAI_API_KEY=your_key
POLYGON_API_KEY=your_key
JWT_SECRET=your_secret
STRIPE_SECRET=your_stripe_key
DATABASE_URL=sqlite:///app.db
---

## to run backend 
uvicorn backend.main:app --reload

# to run frontend
streamlit run frontend/app.py


## 🏗️ Architecture Overview
