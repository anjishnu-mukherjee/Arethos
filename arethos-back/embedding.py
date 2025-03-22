import os
from pinecone import Pinecone
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import Settings

# Setting up LLM and Embeddings
llm = Gemini(api_key=os.environ["GEMINI_API_KEY"])
llm_embedding = GeminiEmbedding(model_name="models/embedding-001")

Settings.llm = llm
Settings.embed_model = llm_embedding
Settings.chunk_size = 1024

# Initialize Pinecone Client
pinecone_client = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
index = pinecone_client.Index(name="arethos-a")

def get_gemini_embedding(text):
    return llm_embedding.get_text_embedding(text)

def retrieve_relevant_vector(query_text, top_k=2):

    query_embedding = get_gemini_embedding(query_text)

    # Search for similar vectors in Pinecone
    response = index.query(
        vector=query_embedding,
        top_k=top_k,  
        include_metadata=True 
    )

    # Extract and return results
    matches = response.get("matches", [])
    if matches:
        return matches 
    else:
        return None