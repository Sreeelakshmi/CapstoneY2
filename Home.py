import streamlit as st

# Set page config
st.set_page_config(page_title="Eastern Trails", page_icon="🌄", layout="wide")

# Custom CSS for better layout
st.markdown(
    """
    <style>
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 20px;
            background-color: #f0f0f0;
            border-bottom: 2px solid #ddd;
        }
        .title-container {
            display: flex;
            align-items: center;
            gap: 15px;
        }
        .header-logo {
            height: 60px;
        }
        .header-title {
            font-size: 28px;
            font-weight: bold;
            color: #2f3e46;
        }
        .header-buttons button {
            margin-left: 10px;
            padding: 8px 15px;
            background-color: #6a994e;
            color: white;
            border: none;
            border-radius: 20px;
            cursor: pointer;
            font-weight: bold;
        }
        .header-buttons button:hover {
            background-color: #52796f;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
with st.container():
    col1, col2 = st.columns([0.7, 0.3])

    with col1:
        st.markdown(
            """
            <div class="title-container">
                <img src="assets/eastern_trails_logo.png" class="header-logo">
                <span class="header-title">Eastern Trails</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        col_btn1, col_btn2 = st.columns([1, 1])
        with col_btn1:
            if st.button("Sign In"):
                st.write("Sign In clicked!")
        with col_btn2:
            if st.button("Sign Up"):
                st.write("Sign Up clicked!")

# Subtitle
st.markdown("""
## Discover the Heart of NorthEast India, One Trail at a Time.
""")

# Section buttons (like cards)
st.markdown("### Explore Our Features")

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

# Footer
st.markdown("---")
st.write("🚀 Developed with ❤️ for travel enthusiasts")
