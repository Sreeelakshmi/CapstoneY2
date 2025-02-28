import streamlit as st

# Set page config
st.set_page_config(page_title="Eastern Trails - Travel Advisor", layout="wide")

# Custom CSS for colors and styling
st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
        }
        .main-title {
            font-size: 45px;
            font-weight: bold;
            color: #2f4858; /* Deep Blue */
            text-align: center;
            margin-top: 10px;
        }
        .sub-title {
            font-size: 20px;
            color: #4f7942; /* Forest Green */
            text-align: center;
            margin-bottom: 30px;
        }
        .button {
            background-color: #f4a261; /* Warm Orange */
            color: white;
            border: none;
            padding: 12px 30px;
            text-align: center;
            font-size: 16px;
            border-radius: 5px;
            margin: 10px;
            cursor: pointer;
        }
        .button:hover {
            background-color: #e76f51; /* Reddish-Orange */
        }
        .top-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 30px;
            background-color: #2f4858; /* Deep Blue */
            color: white;
        }
        .top-bar img {
            height: 60px;
        }
        .top-bar button {
            background-color: #f4a261;
            color: white;
            border: none;
            padding: 8px 16px;
            margin-left: 10px;
            cursor: pointer;
            border-radius: 5px;
        }
        .feature-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Top Bar with Logo and Sign In / Login
col1, col2 = st.columns([0.7, 0.3])
with col1:
    st.image("Bown and Yellow Vintage Adventure logo (3).png", width=100)  # Logo you uploaded
with col2:
    st.write("""
        <div class="top-bar">
            <div>
                <button onclick="alert('Sign In clicked')">Sign In</button>
                <button onclick="alert('Login clicked')">Login</button>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Title and Subtitle
st.markdown('<div class="main-title">Welcome to Eastern Trails</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">One Trail at a Time - Explore the Beauty of North East India</div>', unsafe_allow_html=True)

# Feature Buttons
st.markdown('<div class="feature-container">', unsafe_allow_html=True)

features = [
    ("Travel Itinerary", "travel_itenary.py"),
    ("Tourist Attractions", "tourist.py"),
    ("Weather Info", "weather.py"),
    ("Group Planning", "group_planning.py"),
    ("Chatbot Assistance", "chatbot.py"),
    ("Travel Blog", "blog.py"),
    ("Travel Trivia", "trivia.py"),
    ("Fun Games", "game.py"),
    ("Souvenir Guide", "souvenirs.py")
]

for feature, file in features:
    st.write(f"""
        <a href="/{file}" target="_self">
            <button class="button">{feature}</button>
        </a>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.write("---")
st.write("🌏 Crafted with ❤️ for Travel Enthusiasts | Explore North East India")

