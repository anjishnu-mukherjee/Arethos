from google import genai
import os

# keep the contxt before the questions
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

prompt = """

**Past Similar Grading Examples:**
Make use of this information to grade the following answers:
    Question: What is the name of the boy who plays guitar?  
    Feedback: Correct! Anjishnu is mentioned as a musician and a guitarist in the passage. Well done!  
    Score: 10/10 

    Question: What instrument does Anjishnu play?  
    Feedback: Correct! The passage explicitly states that Anjishnu plays the guitar.  
    Score: 10/10  

Here is the comprehension :
    Arjun is deeply passionate about music and spends most of his free time strumming his guitar. 
    He enjoys experimenting with different melodies and often performs at school events. 
    His dream is to become a renowned guitarist and inspire others with his music.

**New Question:**
    1. What is the name of the boy?
    A: The boy's name is anjishnu.

    2. What instrument does he play?
    A: He plays the guitar.


Evaluate each question indivisually and provide feedback and grade for each question in this format:
Question Number : Grade/10
Feedback: Your feedback here
"""

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt,
)

print(response.text)