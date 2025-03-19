def convert_question_paper_to_list(questions : str):
    raw_lines = questions.splitlines()
    section_list = []
    i = 0
    j = 1

    while(j<len(raw_lines)):
        if "SECTION" in raw_lines[i] and "SECTION" in raw_lines[j]:
            section_list.append("\n".join(raw_lines[i+1:j-1]))
            i = j
            j = i+1
        if  "SECTION" not in raw_lines[i]:
            i+=1
        if  "SECTION" not in raw_lines[j]:
            j+=1
        

    return section_list

def convert_answers_to_list(answers:str):
    raw_lines = answers.splitlines()
    answer_sections = []
    i = 0
    j = 1

    while(j<len(raw_lines)):
        if "SECTION" in raw_lines[i] and "SECTION" in raw_lines[j]:
            answer_sections.append("\n".join(raw_lines[i+1:j-1]))
            i = j
            j = i+1
        if  "SECTION" not in raw_lines[i]:
            i+=1
        if  "SECTION" not in raw_lines[j]:
            j+=1
    
    return answer_sections

def get_similar_questions(prompt : str) -> str:
    #TODO
    """
    This function will take a prompt (question answer string) and return top K similar questions from the pinecone database.
    Join the K responses using "\n" and return as a string.
    """
    return ""

def get_prompt_list(questions : str,answers : str):
    question_list = convert_question_paper_to_list(questions)
    answers_list = convert_answers_to_list(answers)

    prompt_list = []

    for i in range(len(question_list)):
        raw_prompt = f"""
        {question_list[i]}
        {answers_list[i]}
                """
        similars = get_similar_questions(raw_prompt)

        prompt =f"""
                {similars}\n
                {raw_prompt}
                """
        prompt_list.append(prompt)

    return prompt_list

def generate_gemini_resp(question:str, answers:str):

    prompt_list = get_prompt_list(question,answers)
    response_list = [];

    #TODO
    """
    Use the prompt_list to generate responses using the Google's Gemini model.
    Append the responses to the response_list as a dict in the following format:
    response_list : [
            { 
                "question":<>,
                "answer":<>
            },
            ...
            ]
    """

    return response_list

