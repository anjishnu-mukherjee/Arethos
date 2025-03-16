# Arethos

Alpha testing branch - Pinecone implementation for storing and reteriving similar responses

`pip install -r requirements.txt`

## Testing - Alpha:

embedding.py
> Converts text into vector embeding

pine.py
> Pinecone initialzation containing functions to upload and fetch from the pinecone database

upload_data.py
> Reads the `comprehension.txt` file to read the data to upload to the pinecone database
> 
> comprehension.txt - format
>```
> $$
> <QUERY>
> $$
> .....
> ```
fetch_simiar.py
> Given a new query retrives the top 5 similar resposes and writes it to `similar_responses.txt`


