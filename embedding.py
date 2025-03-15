import re
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

def extract_qa_blocks(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    pattern = re.findall(r'Question: (.*?)\nStudent Answer: (.*?)\nFeedback: (.*?)\nScore: (\d+/10)', text, re.DOTALL)

    qa_blocks = []
    for match in pattern:
        question, answer, feedback, score = match
        qa_text = f"Question: {question}\nStudent Answer: {answer}\nFeedback: {feedback}\nScore: {score}"
        qa_blocks.append({
            "question": question, 
            "answer": answer, 
            "feedback": feedback, 
            "score": score, 
            "full_text": qa_text
        })
    
    return qa_blocks

def embed_and_store(file_path, enable_embedding=True):
    qa_blocks = extract_qa_blocks(file_path)
    
    # Retrieve existing IDs from Pinecone
    existing_ids = set()
    index_stats = index.describe_index_stats()
    
    if "namespaces" in index_stats and index_stats["namespaces"]:
        for namespace in index_stats["namespaces"]:
            existing_vectors = index.fetch(ids=[str(i) for i in range(len(qa_blocks))])
            existing_ids.update(existing_vectors.vectors.keys())

    vectors = []
    if enable_embedding:
        for i, qa in enumerate(qa_blocks):
            if str(i) in existing_ids:
                print(f"Skipping Q&A {i} (Already exists in Pinecone)")
                continue

            embedding = get_gemini_embedding(qa["full_text"])
            vectors.append((str(i), embedding, {"feedback": qa["feedback"], "score": qa["score"]}))
        
        # Upload to Pinecone if there are new vectors
        if vectors:
            index.upsert(vectors=vectors)
            print(f"Successfully stored {len(vectors)} new Q&A embeddings in Pinecone.")
        else:
            print("No new Q&A blocks to add.")
    else:
        print("Skipping embedding as per user request.")


