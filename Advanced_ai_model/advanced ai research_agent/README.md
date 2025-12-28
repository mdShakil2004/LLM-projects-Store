# 🔍 Advanced Multi-Agent AI Researcher

A powerful **multi-agent research system** built using **Streamlit + Agno**, capable of performing real-time research across:
> 📌 This project demonstrates real-world **multi-agent AI orchestration**, research automation, and LLM-powered analysis pipelines used in modern AI products.

- 🧠 Hacker News  
- 🌐 Web (DuckDuckGo search)  
- 📰 Full article analysis  
- 🐦 X (Twitter) sentiment & discussions  

The project supports **two modes**:
1. ☁️ Cloud-based using **OpenAI GPT-4o**
2. 🖥️ Fully local using **LLaMA 3.1 (via Ollama)**

It coordinates multiple specialized AI agents to generate **structured, source-backed research reports**.

---

## 🚀 Features

✅ Multi-agent collaboration  
✅ Real-time web + social research  
✅ HackerNews trend analysis  
✅ Article reading & summarization  
✅ X (Twitter) sentiment & influencer insights  
✅ Source citations  
✅ Streaming output  
✅ Clean Streamlit UI  
✅ Debug / agent trace mode  
✅ Works with OpenAI or fully local LLMs  

---
<img width="1209" height="860" alt="image" src="https://github.com/user-attachments/assets/22b7bb41-a08f-4636-9417-3388c618254b" />
<img width="1217" height="891" alt="image" src="https://github.com/user-attachments/assets/09a34bb9-8941-4c65-94df-9919f3e0cd8f" />


## 🧠 Agent Architecture

Each agent has a focused responsibility:

| Agent | Responsibility |
|------|----------------|
| **HackerNews Researcher** | Finds top stories & discussions |
| **Web Searcher** | Performs live web search & fact verification |
| **Article Reader** | Reads and analyzes full articles |
| **X Researcher** | Tracks real-time discussions, sentiment & influencers |
| **Team Lead (Coordinator)** | Plans, validates, and compiles final report |

---

## 📊 Output Structure

Each query produces a well-structured research report:

- **Executive Summary**
- **Key Findings**
- **Insights from X / Twitter**
- **Notable Quotes**
- **Sources**

---

## Uses:
gpt-4o-2024-11-20
Real-time multi-agent orchestration
Best quality reasoning

### Install dependencies
  ```bash
  pip install streamlit agno newspaper4k duckduckgo-search
  streamlit run filename
#install locally
ollama serve
ollama pull llama3.1:70b



