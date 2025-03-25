import azure.functions as func
import json
import logging
from parse_question import generate_gemini_resp

app = func.FunctionApp()
import json
import logging
import azure.functions as func



# os.environ["GEMINI_API_KEY"] = GEMINI_API
# os.environ["PINECONE_API_KEY"] = PINECONE_API

@app.route(route="geminiResponse", auth_level=func.AuthLevel.FUNCTION)
def geminiResponse(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Handle CORS preflight request (OPTIONS request)
    if req.method == "OPTIONS":
        return func.HttpResponse(
            status_code=200,
            headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            }
        )

    question = req.params.get('questions')
    answers = req.params.get('answers')  # 🔹 Fix incorrect key

    if not question or not answers:
        try:
            req_body = req.get_json()
            question = str(req_body.get('questions', question))  # Use fallback if missing
            answers = str(req_body.get('answers', answers))  # 🔹 Fix incorrect key

            # print(f"Received questions: {question}")
            # print(f"Received answers: {answers}")
        except ValueError:
            return func.HttpResponse(
                json.dumps({"error": "Missing questions or answers parameter"}),
                status_code=400,
                mimetype="application/json",
                headers={"Access-Control-Allow-Origin": "*"}
            )

    try:
        response_data = generate_gemini_resp(question, answers)

        return func.HttpResponse(
            json.dumps(response_data, indent=4),
            mimetype="application/json",
            headers={"Access-Control-Allow-Origin": "*"}  # 🔹 Allow CORS
        )

    except Exception as e:
        logging.error(f"Error generating response: {e}")
        return func.HttpResponse(
            json.dumps({"error": f"Internal Server Error: {str(e)}"}),
            status_code=500,
            mimetype="application/json",
            headers={"Access-Control-Allow-Origin": "*"}
        )
