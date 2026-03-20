from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Step 1: Reviews (you can change later)
reviews = [
    "The food was delicious and fresh",
    "Service was very slow",
    "Amazing ambiance and great staff",
    "The pizza was excellent",
    "Very expensive for the quality",
    "Staff was rude and unhelpful",
    "food was terrible",
    "bad quality food",
    "worst meal ever"
]

# Step 2: Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Step 3: Convert reviews to embeddings
embeddings = model.encode(reviews)

# Step 4: Check shape
print("Embedding shape:", embeddings.shape)

# Step 5: Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

# Step 6: Add embeddings to index
index.add(np.array(embeddings))

# Step 7: Query
query = "bad food"
query_vector = model.encode([query])

# Step 8: Search
k = 2
distances, indices = index.search(np.array(query_vector), k)

# Step 9: Print results
print("\nQuery:", query)
print("Top results:")
for i in indices[0]:
    print("-", reviews[i])