import azure.functions as func
import json
import logging
from parse_question import generate_gemini_resp

app = func.FunctionApp()

@app.route(route="geminiResponse", auth_level=func.AuthLevel.FUNCTION)
def gemini_response(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    question = req.params.get('questions')
    answers = req.params.get('answers')

    if not question:
        try:
            req_body = req.get_json()
        except ValueError:
            # send back a http error response that parameter is missing
            return func.HttpResponse("Missing questions parameter", status_code=400)
        else:
            question = req_body.get('questions')
    
    if not answers:
        try:
            req_body = req.get_json()
        except ValueError:
            return func.HttpResponse("Missing answers parameter", status_code=400)
        else:
            answers = req_body.get('answers')
    

    try:
        return func.HttpResponse(json.dumps(generate_gemini_resp(question,answers), indent=4), mimetype="application/json")

    except Exception as e:
        logging.error(f"Error fetching news: {e}")
        return func.HttpResponse(f"Internal Server Error: {e}", status_code=500)