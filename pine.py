from pinecone import Pinecone, ServerlessSpec
from keys import PINECONE_API
from embedding import get_text_embedding

pc = Pinecone(api_key=PINECONE_API)


def upload_to_pinecone(uid,index_name,raw_txt):

    embedding = get_text_embedding(raw_txt)

    # if index_name not in pc.list_indexes():
    if not pc.has_index(index_name):
    # try:
        pc.create_index(index_name, dimension=384, metric="cosine",spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        ) 
        )
    # except :
        print(f"Creating the Index {index_name}")
    
    index = pc.Index(index_name)

    index.upsert([
        (uid, embedding, {"source": raw_txt}) 
    ])


def get_similar_result(index_name,text):
    index = pc.Index(index_name)
    vector = get_text_embedding(text)
    result = index.query(
        vector=vector,
        top_k=5,  
        include_metadata=True  
    )

    responses = []
    for match in result["matches"]:
        responses.append(f"ID: {match['id']}, Score: {match['score']}, Metadata: {match.get('metadata', {})}")

    return responses