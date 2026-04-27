from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# -----------------------------
# 1. Load embedding model
# -----------------------------
model = SentenceTransformer('all-MiniLM-L6-v2')

# -----------------------------
# 2. Your sample data
# -----------------------------
text = """
Apple is a technology company known for iPhones and MacBooks.
Google is known for its search engine and AI research.
Amazon is a leader in e-commerce and cloud computing.
Microsoft develops Windows OS and Azure cloud services.
Meta focuses on social media platforms like Facebook and Instagram.
"""

# -----------------------------
# 3. Chunking (VERY IMPORTANT)
# -----------------------------
import re

def chunk_text(text):
    sentences = re.split(r'[.\n]', text)
    chunks = [s.strip() for s in sentences if s.strip()]
    return chunks

chunks = chunk_text(text)

print("Chunks:")
for i, c in enumerate(chunks):
    print(f"{i}: {c}")

# -----------------------------
# 4. Convert chunks to embeddings
# -----------------------------
embeddings = model.encode(chunks)

# -----------------------------
# 5. Create FAISS index
# -----------------------------
dimension = embeddings.shape[1]   # IMPORTANT
index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings))

# -----------------------------
# 6. Query function
# -----------------------------
def search(query, top_k=2):
    query_embedding = model.encode([query])
    
    distances, indices = index.search(np.array(query_embedding), top_k)
    
    results = []
    for idx in indices[0]:
        results.append(chunks[idx])
    
    return results

# -----------------------------
# 7. Test query
# -----------------------------
query = "Which company works in cloud computing?"

results = search(query)

print("\nQuery:", query)
print("\nTop Results:")
for r in results:
    print("-", r)