from transformers import pipeline

generator = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_answer(query, context_docs):
    context = " ".join(context_docs)

    prompt = f"""
You are a legal assistant for Indian law.

Context:
{context}

Question:
{query}

Give a clear and accurate answer:
"""

    result = generator(prompt, max_length=200, do_sample=False)

    return result[0]['generated_text']