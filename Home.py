import streamlit as st

# Set page configuration
st.set_page_config(page_title="Eastern Trails", page_icon="🌄", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px;
            background-color: #f9f5f0;
            border-bottom: 2px solid #ddd;
        }
        .logo {
            height: 70px;
        }
        .button-container {
            display: flex;
            gap: 10px;
        }
        .header-button {
            padding: 8px 15px;
            background-color: #6a994e;
            color: white;
            border: none;
            border-radius: 20px;
            cursor: pointer;
            font-weight: bold;
        }
        .header-button:hover {
            background-color: #4f7c3f;
        }
        .main-title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            margin: 20px 0;
            color: #2f3e46;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #52796f;
            margin-bottom: 30px;
        }
        .section-container {
            display: flex;
            justify-content: center;
            gap: 30px;
            flex-wrap: wrap;
            margin-top: 30px;
        }
        .section-card {
            width: 250px;
            height: 100px;
            background-color: #f0ead6;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            color: #3e403f;
            cursor: pointer;
            transition: all 0.3s;
            text-align: center;
        }
        .section-card:hover {
            background-color: #d6cdbf;
            transform: translateY(-5px);
        }
        .footer {
            text-align: center;
            margin-top: 40px;
            font-size: 14px;
            color: #888;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Header with Logo and Sign In/Sign Up
st.markdown(
    """
    <div class="header-container">
        <img src="https://raw.githubusercontent.com/user/repo/main/EasternTrailsLogo.png" class="logo">
        <div class="button-container">
            <button class="header-button" onclick="alert('Sign In clicked!')">Sign In</button>
            <button class="header-button" onclick="alert('Sign Up clicked!')">Sign Up</button>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Main Title
st.markdown('<div class="main-title">Eastern Trails</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Discover the Heart of NorthEast India, One Trail at a Time.</div>', unsafe_allow_html=True)

# Section Buttons (as clickable cards)
sections = [
    ("📅 Travel Itinerary", "pages/travel_itinerary.py"),
    ("🤖 Chat with TravelBot", "pages/chatbot.py"),
    ("🏅 Travel Trivia", "pages/trivia.py"),
    ("☀️ Check Weather", "pages/weather.py"),
    ("🗺️ Tourist Guide", "pages/tourist_guide.py"),
    ("🎁 Souvenirs", "pages/souvenirs.py"),
]

st.markdown('<div class="section-container">', unsafe_allow_html=True)

for label, page in sections:
    st.markdown(
        f"""
        <div class="section-card" onclick="window.location.href='/{page}'">
            {label}
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">🚀 Developed with ❤️ for travel enthusiasts</div>', unsafe_allow_html=True)
