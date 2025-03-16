from sentence_transformers import SentenceTransformer

def get_text_embedding(text):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embedding = model.encode(text).tolist()
    return embedding
