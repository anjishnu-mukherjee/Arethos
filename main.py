import embedding
from pinecone import Pinecone
import google.generativeai as genai
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import Settings

embedding.embed_and_store("embeddingQnA.txt", enable_embedding=True) 

index = embedding.pinecone_client.Index(name="arethos-a")
print(index.describe_index_stats())

