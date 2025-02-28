import streamlit as st

# Set page title and icon
st.set_page_config(page_title="Eastern Trails", page_icon="🌄", layout="wide")

# Custom CSS for styling the header
st.markdown(
    """
    <style>
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 20px;
            background-color: #E6F2E6;
            border-bottom: 2px solid #618264;
        }
        .logo {
            height: 80px;
        }
        .button-container {
            display: flex;
            gap: 10px;
        }
        .header-button {
            padding: 8px 15px;
            background-color: #618264;
            color: white;
            border: none;
            border-radius: 20px;
            cursor: pointer;
            font-weight: bold;
        }
        .header-button:hover {
            background-color: #4E6B4F;
        }
    </style>
    """, 
    unsafe_allow_html=True
)

# Header Layout - Logo + Sign In/Sign Up
st.markdown(
    """
    <div class="header-container">
        <img src="Dataset and Database/logo.png" class="logo">
        <div class="button-container">
            <form action="#" method="get">
                <button class="header-button" type="button" onclick="alert('Sign In clicked!')">Sign In</button>
            </form>
            <form action="#" method="get">
                <button class="header-button" type="button" onclick="alert('Sign Up clicked!')">Sign Up</button>
            </form>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Main Title and Subtitle
st.title("🌄 Eastern Trails")
st.subheader("Discover the heart of NorthEast India, One Trail at a Time.")

# Description
st.write("""
Explore personalized recommendations, check the weather, get guided itineraries, chat with our AI bot, play travel trivia, and even shop for souvenirs!
Select a section below to begin your adventure.
""")

# Buttons for navigating to pages
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📅 Travel Itinerary"):
        st.switch_page("pages/travel_itinerary.py")

    if st.button("🤖 Chat with TravelBot"):
        st.switch_page("pages/chatbot.py")

    if st.button("🏅 Travel Trivia"):
        st.switch_page("pages/trivia.py")

with col2:
    if st.button("☀️ Check Weather"):
        st.switch_page("pages/weather.py")

    if st.button("🗺️ Tourist Guide"):
        st.switch_page("pages/tourist_guide.py")

    if st.button("🎁 Souvenirs"):
        st.switch_page("pages/souvenirs.py")

st.markdown("---")
st.write("🚀 Developed with ❤️ for travel enthusiasts")
