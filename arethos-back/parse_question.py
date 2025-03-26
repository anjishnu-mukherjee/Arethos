import json
import os
import re
from dotenv import load_dotenv
from google import genai
from embedding import retrieve_relevant_vector

load_dotenv()
def convert_question_paper_to_list(questions: str):
    """Extracts individual questions from a structured question paper format."""
    raw_lines = questions.splitlines()
    section_list = []
    current_section = []

    for line in raw_lines:
        if line.startswith("SECTION"):
            if current_section:
                section_list.extend(current_section)
            current_section = []
        elif line.strip():
            current_section.append(line.strip())

    if current_section:
        section_list.extend(current_section)
    
    # print("Section list:", len(section_list))
    return ["\n".join(section_list)]

def convert_answers_to_list(answers: str):
    """Extracts individual answers corresponding to the questions."""
    raw_lines = answers.splitlines()
    answer_list = []
    current_section = []

    for line in raw_lines:
        if line.startswith("SECTION"):
            if current_section:
                answer_list.extend(current_section)
            current_section = []
        elif line.strip():
            current_section.append(line.strip())

    if current_section:
        answer_list.extend(current_section)

    # print("Answer list:", len(answer_list))

    return ["\n".join(answer_list)]

def get_similar_questions(prompt : str) -> str:
    matches = retrieve_relevant_vector(prompt, top_k=2) or []
    similars = ""
    for match in matches:
        metadata = match.get("metadata", {})
        similars += f"Question: {metadata.get('question', 'N/A')}\n"
        similars += f"Answer: {metadata.get('answer', 'N/A')}\n"
        similars += f"Feedback: {metadata.get('feedback', 'N/A')}\n"
        similars += f"Score: {metadata.get('score', 'N/A')}\n\n"
    
    return similars.strip()

def get_prompt_list(questions: str, answers: str):
    """Generates individual prompts for each question-answer pair."""
    question_list = convert_question_paper_to_list(questions)
    answer_list = convert_answers_to_list(answers)

    if len(question_list) != len(answer_list):
        raise ValueError("Mismatch between the number of questions and answers.")

    prompt_list = []

    for i in range(len(question_list)):
        raw_prompt = f"""
        Question: {question_list[i]}
        Answer: {answer_list[i]}
        """

        similars = get_similar_questions(raw_prompt)

        prompt = f"""
        {similars}\n
        {raw_prompt}
        """
        prompt_list.append(prompt)

    return prompt_list

def generate_gemini_resp(questions: str, answers: str):
    prompt_list = get_prompt_list(questions, answers)
    print("comming here")
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    print("passing this")
    response_list = []

    for prompt in prompt_list:
        json_prompt = f"""
        Given the following question and student answer, provide a structured JSON response.
        Format:
        {{
            "context": "Explanation of grading criteria",
            "qa_pairs": [
                {{
                    "question": "Original question",
                    "answer": "Student's answer",
                    "feedback": "Detailed feedback",
                    "score": "Numeric score out of 10"
                }}
            ]
        }}
        
        {prompt}
        """

        response = client.models.generate_content(model="gemini-2.0-flash", contents=json_prompt)
        raw_text = response.text.strip()
        cleaned_text = re.sub(r"^```json|```$", "", raw_text).strip()

        try:
            json_data = json.loads(cleaned_text)
            response_list.append({
                "context": json_data.get("context", ""),
                "qa_pairs": json_data.get("qa_pairs", [])
            })
        except json.JSONDecodeError:
            print("Error: Could not parse JSON from Gemini response.")
            print("Raw response:", raw_text)

    return response_list
