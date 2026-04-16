# ⚖️ Legal RAG Assistant (Indian Constitution)

A Retrieval-Augmented Generation (RAG) based legal assistant built using open-source models to answer questions related to the Constitution of India.

---

## 🚀 Features
 
* 🔍 Semantic search using FAISS
* 🧠 Legal embeddings with InLegalBERT
* 🤖 Answer generation using FLAN-T5
* 📚 Custom dataset (Indian Constitution Q&A)
* 💬 Interactive CLI chatbot

---

## 🏗️ Architecture

```
User Query → Embedding → FAISS Retrieval → Context → LLM → Answer
```

---

## 📂 Dataset

Uses a structured JSON dataset:

```json
{
  "question": "...",
  "answer": "..."
}
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/legal-rag-assistant.git
cd legal-rag-assistant

pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python src/main.py
```

---

## 💡 Example

```
Ask your legal question: What is Article 21?

Answer:
Article 21 guarantees the right to life and personal liberty...
```

---

## 📌 Models Used

* `law-ai/InLegalBERT` → embeddings
* `google/flan-t5-base` → generation
* `FAISS` → vector search

---

## 🔧 Future Improvements

* Add Streamlit UI
* Add chat memory
* Use better LLMs (Mistral / LLaMA)
* Hybrid search (BM25 + vector)
* Reranking with CrossEncoder

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first.

---

## 📜 License

MIT License
