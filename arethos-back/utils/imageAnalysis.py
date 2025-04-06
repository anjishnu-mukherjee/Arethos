import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  

model = genai.GenerativeModel('gemini-2.0-flash')

def analyze_image(image_data, prompt="respond me with just the text in the image."):
    try:
        parts = [
            prompt,
            {
                "mime_type": "image/jpeg",  
                "data": image_data
            }
        ]

        response = model.generate_content(parts)
        return response.text

    except Exception as e:
        return f"An error occurred: {e}"