# ⚖️ Legal RAG Assistant (Indian Constitution)

A **Retrieval-Augmented Generation (RAG)** based legal assistant that answers questions related to the **Constitution of India** using open-source models.

This project combines **semantic search (FAISS)** with **large language models (LLMs)** to deliver accurate, context-aware legal responses.

---

## 📖 Overview

Traditional LLMs often hallucinate or lack domain-specific knowledge. This project solves that by:

* Retrieving **relevant legal context** from a curated dataset
* Feeding that context into a **language model**
* Generating **accurate and grounded answers**

It is designed as a **lightweight, open-source legal QA system** for learning and experimentation.

---

## 🚀 Features

* 🔍 **Semantic Search** using FAISS for fast vector similarity lookup
* 🧠 **Domain-Specific Embeddings** powered by InLegalBERT
* 🤖 **Answer Generation** using FLAN-T5 (instruction-tuned LLM)
* 📚 **Custom Dataset** based on Indian Constitution Q&A
* 💬 **Interactive CLI Chatbot** for real-time querying
* ⚡ Fully **open-source and reproducible pipeline**

---

## 🏗️ Architecture

```text
User Query
   ↓
Embedding (InLegalBERT)
   ↓
FAISS Vector Search
   ↓
Top-K Relevant Documents
   ↓
Context Injection
   ↓
FLAN-T5 (LLM)
   ↓
Final Answer
```

---

## 📂 Project Structure

```bash
legal-rag-assistant/
│
├── data/
│   └── constitution_qa.json      # Dataset
│
├── src/
│   ├── embeddings.py             # Embedding logic
│   ├── retrieval.py              # FAISS search
│   ├── generator.py              # LLM generation
│   └── main.py                   # CLI app
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Dataset

The system uses a structured JSON dataset containing legal question-answer pairs.

### Example:

```json
{
  "question": "What is Article 21?",
  "answer": "Article 21 guarantees the right to life and personal liberty."
}
```

You can extend the dataset with:

* More constitutional articles
* Case laws
* Legal explanations

---

## ⚙️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/mdShakil2004/LLM-projects-Store.git
cd indian_contitution_law

pip install -r requirements.txt
```

---

## ▶️ Usage

Run the CLI chatbot:

```bash
python src/main.py
```

You can now ask legal questions interactively.

---

## 💡 Example

```text
Ask your legal question: What is Article 21?

Answer:
Article 21 guarantees the right to life and personal liberty and ensures that no person shall be deprived of life except according to procedure established by law.
```

---

## 🧠 Models Used

| Component     | Model/Tool            | Purpose                      |
| ------------- | --------------------- | ---------------------------- |
| Embeddings    | `law-ai/InLegalBERT`  | Legal semantic understanding |
| Generation    | `google/flan-t5-base` | Answer generation            |
| Vector Search | `FAISS`               | Fast similarity search       |

---

## ⚡ How It Works

1. The user enters a legal query
2. The query is converted into a vector using **InLegalBERT**
3. FAISS retrieves the most relevant documents
4. Retrieved context is passed to **FLAN-T5**
5. The model generates a grounded, contextual answer

---

## 🔧 Future Improvements

* 🌐 Build a **Streamlit / Web UI**
* 🧠 Add **chat memory (multi-turn conversations)**
* 🚀 Integrate **advanced LLMs** (Mistral, LLaMA, Mixtral)
* 🔀 Implement **Hybrid Search (BM25 + Vector)**
* 🎯 Add **Reranking (Cross-Encoder)**
* 📈 Introduce **evaluation metrics (accuracy, recall)**
* ⚡ Cache embeddings for faster performance

---

## 🤝 Contributing

Contributions are welcome!

### Steps:

1. Fork the repository
2. Create a new branch (`feature/your-feature`)
3. Commit your changes
4. Open a Pull Request

For major changes, please open an issue first to discuss.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## ⭐ Support

If you found this project useful:

* ⭐ Star the repository
* 🍴 Fork it
* 📢 Share with others

---

## 🙌 Acknowledgements

* Hugging Face Transformers
* FAISS (Facebook AI Similarity Search)
* Open-source legal datasets

---

## 📬 Contact

For queries or collaboration:

* GitHub: https://github.com/mdShakil2004

---

**Built with ❤️ for learning and open-source contribution**
