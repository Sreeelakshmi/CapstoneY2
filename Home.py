import streamlit as st
import sys

# Set page title and icon
st.set_page_config(page_title="Travel Advisor", page_icon="🌍", layout="wide")

# Header
st.title("🌍 Welcome to Your Travel Advisor")
st.subheader("Plan your perfect trip with ease and fun!")

# Description
st.write("""
Explore personalized recommendations, check the weather, get guided itineraries, chat with our AI bot, play travel trivia, and even shop for souvenirs!
Select a section below to begin your adventure.
""")

# Check Streamlit version for compatibility
def is_switch_page_supported():
    import streamlit
    version = tuple(map(int, streamlit.__version__.split(".")))
    return version >= (1, 18)

# Navigation helper function
def navigate_to_page(page_path):
    if is_switch_page_supported():
        try:
            st.switch_page(page_path)
        except Exception as e:
            st.error(f"❌ Unable to switch page: {e}")
    else:
        st.error("⚠️ Your Streamlit version is too old for `switch_page()`. Please upgrade to 1.18 or newer.")

# Explain expected folder structure (for debugging)
st.info("""
📂 Expected Folder Structure:
- Home.py (this file)
- pages/
    - travel_itinerary.py
    - chatbot.py
    - trivia.py
    - weather.py
    - tourist_guide.py
    - souvenirs.py
Make sure this structure exists for navigation to work.
""")

# Create buttons/links to each module
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📅 Travel Itinerary"):
        navigate_to_page("pages/travel_itinerary.py")

    if st.button("🤖 Chat with TravelBot"):
        navigate_to_page("pages/chatbot.py")

    if st.button("🏅 Travel Trivia"):
        navigate_to_page("pages/trivia.py")

with col2:
    if st.button("☀️ Check Weather"):
        navigate_to_page("pages/weather.py")

    if st.button("🗺️ Tourist Guide"):
        navigate_to_page("pages/tourist_guide.py")

    if st.button("🎁 Souvenirs"):
        navigate_to_page("pages/souvenirs.py")

# Optional Footer
st.markdown("---")
st.write("🚀 Developed with ❤️ for travel enthusiasts")
