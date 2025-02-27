import streamlit as st

# Set page config
st.set_page_config(
    page_title="Travel Advisor - Eastern Trails",
    page_icon="🌏",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
    <style>
        .main {
            background: linear-gradient(to bottom, #87CEEB, #2E8B57);
        }
        .title {
            color: #FFD700;
            font-size: 48px;
            font-weight: bold;
            text-align: center;
            text-shadow: 2px 2px 4px #000000;
        }
        .subheader {
            color: #F5F5F5;
            text-align: center;
            font-size: 20px;
        }
        .nav-button {
            background-color: #8B4513;
            color: white;
            border: none;
            padding: 12px;
            border-radius: 10px;
            cursor: pointer;
            transition: background-color 0.3s ease;
            font-size: 18px;
            width: 100%;
        }
        .nav-button:hover {
            background-color: #FFD700;
            color: #2E8B57;
        }
        .section {
            background-color: rgba(255, 255, 255, 0.8);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }
    </style>
""", unsafe_allow_html=True)

# Display logo centered
col1, col2, col3 = st.columns([1,3,1])
with col2:
    st.image("Dataset and Database/Eastern Trails.png", use_column_width=True)

# Header section with text
st.markdown('<h1 class="title">Explore the Enchanting North East India</h1>', unsafe_allow_html=True)
st.markdown('<p class="subheader">Your personal travel advisor for the mesmerizing North East</p>', unsafe_allow_html=True)

# Main sections for features
st.write("")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    if st.button("📅 Travel Itinerary"):
        st.switch_page("pages/travel_itenary.py")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section">', unsafe_allow_html=True)
    if st.button("🌦️ Weather Forecast"):
        st.switch_page("pages/weather.py")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section">', unsafe_allow_html=True)
    if st.button("🎮 Fun Travel Game"):
        st.switch_page("pages/game.py")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    if st.button("💬 Travel Chatbot"):
        st.switch_page("pages/chatbot.py")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section">', unsafe_allow_html=True)
    if st.button("🎁 Souvenirs Guide"):
        st.switch_page("pages/souvenirs.py")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section">', unsafe_allow_html=True)
    if st.button("👥 Group Planning"):
        st.switch_page("pages/group_planning.py")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    if st.button("🗺️ Tourist Guide"):
        st.switch_page("pages/tourist.py")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section">', unsafe_allow_html=True)
    if st.button("❓ Travel Trivia"):
        st.switch_page("pages/trivia.py")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.write("---")
st.markdown('<p style="text-align:center; color:#F5F5F5;">Crafted with ❤️ by Eastern Trails - ESTD 2025</p>', unsafe_allow_html=True)
