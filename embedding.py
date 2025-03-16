from sentence_transformers import SentenceTransformer

# Load pre-trained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Text to encode
text = "Pinecone makes vector search easy."

# Convert text to vector embedding
embedding = model.encode(text).tolist()

print(embedding)  # Prints the embedding as a list of floats
