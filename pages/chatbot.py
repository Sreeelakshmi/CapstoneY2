import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(prompt)

    return response.text

st.title("Gemini Chatbot")

user_input = st.text_area("Enter your prompt:")

if st.button("Generate"):
    if user_input.strip():
        with st.spinner("Generating response..."):
            response = generate(user_input)
        st.write(response)
    else:
        st.warning("Please enter a prompt.")
