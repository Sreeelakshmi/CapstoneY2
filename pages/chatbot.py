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

    response = model.generate_content(
        f"You are 'Eastern Trails Bot', an expert travel advisor specializing in Northeast India. "
        f"Please provide friendly, expert travel advice about Northeast India, including places to visit, "
        f"cultural experiences, local cuisine, transportation options, and tips for travelers. "
        f"User's question: {prompt}"
    )

    return response.text

# Set page config for better UI
st.set_page_config(page_title="Eastern Trails Travel Advisor", page_icon="🏞️", layout="centered")

# Custom CSS for travel theme
st.markdown("""
    <style>
    .main {
        background-color: #f0f7ff;
    }
    .stTextArea textarea {
        background-color: #ffffff;
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
        background-color: #e6f7ff;
        padding: 15px;
        border-radius: 10px;
        margin-top: 10px;
        font-size: 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }
    .bot-bubble {
        background-color: #fff3cd;
    }
    </style>
""", unsafe_allow_html=True)

# Header with image (updated with use_container_width)
st.image(
    "https://www.tourmyindia.com/states/northeast-india/images/north-east-india-tourism.jpg",
    caption="Explore Northeast India with Eastern Trails",
    use_container_width=True
)

# App Title and Introduction
st.title("🏞️ Eastern Trails Travel Advisor")
st.write("Welcome to **Eastern Trails**, your personal travel guide for exploring the breathtaking destinations of **Northeast India**. From the misty hills of Meghalaya to the vibrant culture of Assam, I'm here to help you plan your adventure!")

# User Input
user_input = st.text_area("🌏 Ask me anything about traveling in Northeast India:", height=100, placeholder="Where should I visit in Meghalaya?")

# Chatbot Response Section
if st.button("✨ Get Travel Tips"):
    if user_input.strip():
        with st.spinner("🔎 Finding the best recommendations..."):
            response = generate(user_input)

        # Display chatbot response in styled bubble
        st.markdown(f"""
        <div class="chat-bubble bot-bubble">
            <strong>Eastern Trails Bot:</strong><br>{response}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter your question or travel query.")

# Footer
st.markdown("---")
st.caption("🌄 Powered by Gemini AI | Brought to you by **Eastern Trails** - Your Travel Companion for Northeast India")
