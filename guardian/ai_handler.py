import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def get_medical_response(prompt):
    disclaimer = os.getenv("DISCLAIMER_TEXT", "")

    try:
        # Configure Gemini API
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

        # Initialize the model
        model = genai.GenerativeModel("gemini-pro")

        # Generate response
        response = model.generate_content(prompt)

        return response.text + f"\n\n{disclaimer}"

    except Exception as e:
        return f"Error: {str(e)}. Please try again later."

# Example usage
prompt = "What are the symptoms of flu?"
print(get_medical_response(prompt))
