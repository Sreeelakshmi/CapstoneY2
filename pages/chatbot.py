import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # If using .env file to load GOOGLE_API_KEY

def generate():
    client = genai.Client(
        api_key=os.getenv("GOOGLE_API_KEY")
    )

    model = "gemini-2.0-flash"
    contents = [
        Content(
            role="user",
            parts=[
                Part.from_text("INSERT_INPUT_HERE"),
            ],
        ),
    ]
    generate_content_config = GenerateContentConfig(
        temperature=1,
        top_p=0.95,
        top_k=40,
        max_output_tokens=8192,
        response_mime_type="text/plain",
    )

    for chunk in client.generate_content(
        model=model,
        contents=contents,
        generation_config=generate_content_config,
        stream=True,
    ):
        print(chunk.text, end="")

generate()
