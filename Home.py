import streamlit as st

# Set page configuration
st.set_page_config(page_title="Eastern Trails", page_icon="🌄", layout="wide")

# Custom CSS for cleaner layout
st.markdown(
    """
    <style>
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 20px;
            background-color: #f5f5f5;
            border-bottom: 2px solid #ddd;
        }
        .title-container {
            display: flex;
            align-items: center;
            gap: 15px;
        }
        .header-logo {
            height: 50px;
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
        .feature-card {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            height: 150px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 15px rgba(0,0,0,0.15);
        }
        .feature-card h3 {
            margin: 0;
            font-size: 18px;
            color: #2f3e46;
        }
        .feature-card p {
            margin: 5px 0 0;
            font-size: 14px;
            color: #555;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Header Section
with st.container():
    col1, col2 = st.columns([0.7, 0.3])

    with col1:
        st.markdown(
            """
            <div class="title-container">
                <img src="Dataset and Database/eastern_trails_logo.png" class="header-logo">
                <span class="header-title">Eastern Trails</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("Sign In"):
                st.write("Sign In clicked!")
        with col_btn2:
            if st.button("Sign Up"):
                st.write("Sign Up clicked!")

# Subtitle
st.markdown("## 🌄 Discover the Heart of NorthEast India, One Trail at a Time.")
st.markdown("---")

# Features Section
st.markdown("### 🌟 Explore Our Features")

# Feature Cards (Using page_link for navigation)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="feature-card">
            <h3>📅 Travel Itinerary</h3>
            <p>Plan your complete trip with customizable itineraries.</p>
        </div>
        """, unsafe_allow_html=True)
    st.page_link("pages/travel_itinerary.py", label="Go to Itinerary", icon="📅")

    st.markdown(
        """
        <div class="feature-card">
            <h3>🤖 Chat with TravelBot</h3>
            <p>Get AI-powered travel recommendations.</p>
        </div>
        """, unsafe_allow_html=True)
    st.page_link("pages/chatbot.py", label="Go to Chatbot", icon="🤖")

with col2:
    st.markdown(
        """
        <div class="feature-card">
            <h3>☀️ Check Weather</h3>
            <p>Stay informed with real-time weather updates.</p>
        </div>
        """, unsafe_allow_html=True)
    st.page_link("pages/weather.py", label="Go to Weather", icon="☀️")

    st.markdown(
        """
        <div class="feature-card">
            <h3>🗺️ Tourist Guide</h3>
            <p>Explore must-visit attractions and hidden gems.</p>
        </div>
        """, unsafe_allow_html=True)
    st.page_link("pages/tourist_guide.py", label="Go to Tourist Guide", icon="🗺️")

with col3:
    st.markdown(
        """
        <div class="feature-card">
            <h3>🏅 Travel Trivia</h3>
            <p>Test your knowledge with fun travel quizzes.</p>
        </div>
        """, unsafe_allow_html=True)
    st.page_link("pages/trivia.py", label="Go to Trivia", icon="🏅")

    st.markdown(
        """
        <div class="feature-card">
            <h3>🎁 Souvenirs</h3>
            <p>Find and shop for authentic regional souvenirs.</p>
        </div>
        """, unsafe_allow_html=True)
    st.page_link("pages/souvenirs.py", label="Go to Souvenirs", icon="🎁")

# Footer
st.markdown("---")
st.write("🚀 Developed with ❤️ for travel enthusiasts")

