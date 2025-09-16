# Full RAG Example

# Imports
from langchain.document_loaders import TextLoader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from transformers import pipeline

# Step 1: Ingestion (use a string for simplicity)
documents = ["Cats are furry and independent pets.", "Dogs are loyal and love playing.", "Birds can fly and sing beautifully."]

# Step 2: Embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(documents)
embeddings_np = np.array(embeddings).astype('float32')

# Step 3: Retrieval setup
index = faiss.IndexFlatL2(embeddings_np.shape[1])
index.add(embeddings_np)

# Query
question = "Tell me about cats."
query_emb = model.encode([question])

# Retrieve top 1
D, I = index.search(query_emb.astype('float32'), k=1)
retrieved = documents[I[0][0]]

# Step 4: Augmentation
prompt = f"Based on this: {retrieved}\nQuestion: {question}"

# Step 5: Generation
generator = pipeline('text-generation', model='gpt2')
response = generator(prompt, max_length=100, num_return_sequences=1)[0]['generated_text']

print("Answer:", response)