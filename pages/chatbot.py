import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate():
    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content("INSERT_INPUT_HERE")

    print(response.text)

generate()
