# 📦 Import all packages at the start
from langchain_community.document_loaders import TextLoader
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import numpy as np
import faiss
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# -------------------------------
# Step 0: Initialize Gemini API (optional, for advanced generation)
# -------------------------------
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# -------------------------------
# Step 1: Document Ingestion
# -------------------------------
loader = TextLoader("knowledge.txt")
documents = loader.load()
# Split into individual lines for better retrieval
texts = [line.strip() for line in documents[0].page_content.split('\n') if line.strip()]
print("✅ Loaded documents:", len(texts), "chunks")

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
# Step 5: Generation (Local with distilgpt2 for free, or Gemini for better quality)
# -------------------------------
use_gemini = input("Use Gemini API for generation? (y/n, default n): ").lower() == 'y'

# Check if Gemini key is available
if use_gemini and not os.getenv("GEMINI_API_KEY"):
    print("⚠️ No Gemini API key found. Using local model instead.")
    use_gemini = False

if use_gemini:
    model = genai.GenerativeModel('gemini-2.5-flash')  # fast and efficient
    response = model.generate_content(prompt)
    print("\n💡 Final Answer (Gemini):\n", response.text)
else:
    generator = pipeline("text-generation", model="distilgpt2")  # lightweight free model
    response = generator(prompt, max_length=80, num_return_sequences=1)[0]["generated_text"]
    print("\n💡 Final Answer (Local):\n", response)