import azure.functions as func
import json
import logging
from utils.parse_question import generate_gemini_resp,get_data_from_file
from utils.blob_storage import generate_sas_token, get_blob_data, clean_tmp

app = func.FunctionApp()

@app.route(route="geminiResponse", auth_level=func.AuthLevel.FUNCTION)
def geminiResponse(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    if req.method == "OPTIONS":
        return func.HttpResponse(
            status_code=200,
            headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            }
        )

    question = req.params.get('question')
    answers = req.params.get('answer')  

    if not question or not answers:
        try:
            # clean_tmp()
            req_body = req.get_json()
            question = str(req_body.get('questions', question)) 
            answers = str(req_body.get('answers', answers))  
            print("Question:",question)
            print("Answer:",answers)
            question_file_path,question_type = get_blob_data(question)
            ans_file_path,answer_type = get_blob_data(answers)

            print("Question file type:",question_type)
            print("Answer file type:",answer_type)

            if question_type != None and answer_type != None:
                question_file_data = get_data_from_file(question_file_path,question_type)
                answer_file_data = get_data_from_file(ans_file_path,answer_type)
            else:
                return func.HttpResponse(
                    json.dumps({"error": "Invalid file type"}),
                    status_code=400,
                    mimetype="application/json",
                    headers={"Access-Control-Allow-Origin": "*"}
                )
            
        except ValueError:

            return func.HttpResponse(
                json.dumps({"error": "Missing questions or answers parameter"}),
                status_code=400,
                mimetype="application/json",
                headers={"Access-Control-Allow-Origin": "*"}
            )

    try:
        response_data = generate_gemini_resp(question_file_data, answer_file_data)
        clean_tmp()
        return func.HttpResponse(
            json.dumps(response_data, indent=4),
            mimetype="application/json",
            headers={"Access-Control-Allow-Origin": "*"}  
        )

    except Exception as e:
        clean_tmp()
        logging.error(f"Error generating response: {e}")
        return func.HttpResponse(
            json.dumps({"error": f"Internal Server Error: {str(e)}"}),
            status_code=500,
            mimetype="application/json",
            headers={"Access-Control-Allow-Origin": "*"}
        )

@app.route(route="sasurl", auth_level=func.AuthLevel.FUNCTION)
def get_sas_url(req: func.HttpRequest) -> func.HttpResponse:
    file_name = req.params.get('filename')
    if not file_name:
        return func.HttpResponse(
            json.dumps({"error": "Missing filename parameter"}),
            status_code=400,
            mimetype="application/json",
            headers={"Access-Control-Allow-Origin": "*"}
        )
    try:

        response_data = generate_sas_token(file_name)
        return func.HttpResponse(
            json.dumps(response_data, indent=4),
            mimetype="application/json",
            headers={"Access-Control-Allow-Origin": "*"}
        )
    except Exception as e:
        logging.error(f"Error generating SAS URL: {e}")
        return func.HttpResponse(
            json.dumps({"error": f"Internal Server Error: {str(e)}"}),
            status_code=500,
            mimetype="application/json",
            headers={"Access-Control-Allow-Origin": "*"}
        )
    
