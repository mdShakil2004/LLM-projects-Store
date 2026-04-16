import json
from retrieval import Retriever
from generator import generate_answer

# Load data
with open("data/constitution_qa.json", "r", encoding="utf-8") as f:
    data = json.load(f)

documents = [f"Q: {item['question']} A: {item['answer']}" for item in data]

# Initialize retriever
retriever = Retriever(documents)

print("💬 Legal Assistant Ready (type 'exit' to quit)\n")

while True:
    query = input("Ask your legal question: ")

    if query.lower() == "exit":
        break

    docs = retriever.search(query)
    answer = generate_answer(query, docs)

    print("\n📌 Answer:\n", answer)
    print("\n" + "-"*50 + "\n")