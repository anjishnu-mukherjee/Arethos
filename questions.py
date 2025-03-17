import json
import os
import re
from google import genai
from embedding import retrieve_relevant_vector

# Load raw text from files
def load_raw_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def format_questions_answers(context_questions_text, answers_text):
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    prompt = f"""
    Convert the following raw text into a structured JSON format with "context" and "qa_pairs" (list of question-answer pairs).
    
    Context and Questions: 
    {context_questions_text}

    Answers:
    {answers_text}

    Ensure the JSON format follows this structure:
    {{
        "context": "...",
        "qa_pairs": [
            {{"question": "...", "answer": "..."}}
        ]
    }}

    **Only return valid JSON output. Do not include any additional text, explanations, or formatting such as markdown.**
    """

    response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)

    # Remove markdown-style triple backticks before parsing JSON
    raw_text = response.text.strip()
    cleaned_text = re.sub(r"^```json|```$", "", raw_text).strip()

    try:
        json_data = json.loads(cleaned_text)
        return json_data
    except json.JSONDecodeError:
        print("Error: Could not parse JSON from Gemini response.")
        print("Raw response:", raw_text)  # Debugging output
        return None



# Generate the grading prompt
def create_grading_prompt(context, qa_pairs):
    prompt = "**Past Similar Grading Examples:**\n"
    prompt += "Make use of this information to grade the following answers:\n\n"

    # Collect all question texts for batch retrieval
    all_questions = [qa["question"] for qa in qa_pairs]
    
    # Retrieve relevant examples from Pinecone
    matches = []
    for question in all_questions:
        matches.extend(retrieve_relevant_vector(question, top_k=2) or [])

    # Add past similar grading examples
    if matches:
        for match in matches:
            metadata = match.get("metadata", {})
            prompt += f"Question: {metadata.get('question', 'No question available')}\n"
            prompt += f"Answer: {metadata.get('answer', 'No answer available')}\n"
            prompt += f"Feedback: {metadata.get('feedback', 'No feedback available')}\n"
            prompt += f"Score: {metadata.get('score', 'No score available')}\n\n"

    # Add comprehension and new questions
    prompt += f"\nHere is the comprehension:\n    {context}\n\n**New Questions:**\n"
    for i, qa in enumerate(qa_pairs, start=1):
        prompt += f"{i}. {qa['question']}\n    A: {qa['answer']}\n\n"

    # Define the grading format
    prompt += "Evaluate each question individually and provide feedback and grade for each question in this format:\n"
    prompt += "Question Number : Grade/10\nFeedback: Your feedback here\n"
    prompt += "Make sure that during grading all the parameters like - incomplete answers, wrong answers, irrelevant answers, etc. are taken into consideration.\n"
    return prompt


# Send request to Gemini Flash 2.0 for grading
def grade_answers(prompt):
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )

    return response.text
