# 📦 Import all packages at the start
from langchain.document_loaders import TextLoader
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import numpy as np
import faiss
import openai
import os

# -------------------------------
# Step 0: Initialize OpenAI API (optional, for advanced generation)
# -------------------------------
openai.api_key = os.getenv("OPENAI_API_KEY")

# -------------------------------
# Step 1: Document Ingestion
# -------------------------------
loader = TextLoader("knowledge.txt")
documents = loader.load()
texts = [doc.page_content for doc in documents]
print("✅ Loaded documents:", texts)

# -------------------------------
# Step 2: Embedding Creation
# -------------------------------
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(texts)
embeddings_np = np.array(embeddings).astype('float32')

# -------------------------------
# Step 3: Retrieval
# -------------------------------
index = faiss.IndexFlatL2(embeddings_np.shape[1])
index.add(embeddings_np)

query = input("Enter your question: ")
query_emb = model.encode([query])
D, I = index.search(query_emb.astype('float32'), k=1)
retrieved_text = texts[I[0][0]]
print("\n🔎 Retrieved:", retrieved_text)

# -------------------------------
# Step 4: Augmentation
# -------------------------------
prompt = f"Based on this info: {retrieved_text}\nAnswer the question: {query}"
print("\n📝 Augmented Prompt:\n", prompt)

# -------------------------------
# Step 5: Generation (Local with distilgpt2 for free, or OpenAI for better quality)
# -------------------------------
use_openai = input("Use OpenAI for generation? (y/n, default n): ").lower() == 'y'

# Check if OpenAI key is available
if use_openai and not openai.api_key:
    print("⚠️ No OpenAI API key found. Using local model instead.")
    use_openai = False

if use_openai:
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # lightweight and affordable
        messages=[{"role": "user", "content": prompt}]
    )
    print("\n💡 Final Answer (OpenAI):\n", response.choices[0].message.content)
else:
    generator = pipeline("text-generation", model="distilgpt2")  # lightweight free model
    response = generator(prompt, max_length=80, num_return_sequences=1)[0]["generated_text"]
    print("\n💡 Final Answer (Local):\n", response)