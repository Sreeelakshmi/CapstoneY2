import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Function to generate content from Gemini
def generate(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(prompt)

    return response.text

# Set page config for better UI
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖", layout="centered")

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stTextArea textarea {
        background-color: #f9f9f9;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 10px 20px;
    }
    .chat-bubble {
        background-color: #f1f1f1;
        padding: 15px;
        border-radius: 10px;
        margin-top: 10px;
        font-size: 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }
    .bot-bubble {
        background-color: #dbe8ff;
    }
    </style>
""", unsafe_allow_html=True)

# App Header
st.title("🤖 Gemini AI Chatbot")
st.write("Ask me anything and I'll respond using Google's **Gemini 1.5 Flash** model.")

# User Input
user_input = st.text_area("💬 Your Prompt:", height=100)

# Chatbot Response Section
if st.button("✨ Generate Response"):
    if user_input.strip():
        with st.spinner("🔎 Generating response... Please wait"):
            response = generate(user_input)

        # Display chatbot response in styled bubble
        st.markdown(f"""
        <div class="chat-bubble bot-bubble">
            <strong>Gemini:</strong><br>{response}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter a prompt before generating.")

# Footer
st.markdown("---")
st.caption("🤖 Powered by Google's Gemini API | Built with ❤️ using Streamlit")

