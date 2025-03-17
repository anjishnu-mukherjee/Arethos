import os
from questions import load_raw_text, format_questions_answers, create_grading_prompt, grade_answers
from google import genai
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import Settings

# embedding.embed_and_store("embeddingQnA.txt", enable_embedding=True) 


client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

context_questions_text = load_raw_text("input/context_questions.txt")
answers_text = load_raw_text("input/answers.txt")

    # Convert to structured format
formatted_data = format_questions_answers(context_questions_text, answers_text)
    
if formatted_data:
    context = formatted_data["context"]
    qa_pairs = formatted_data["qa_pairs"]

        # Generate grading prompt
    grading_prompt = create_grading_prompt(context, qa_pairs)
    grading_result = grade_answers(grading_prompt)

    print("\n===== Grading Result =====\n")
    print(grading_result)
else:
    print("Failed to format questions and answers.")