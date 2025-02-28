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
        .card {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            text-align: center;
            cursor: pointer;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 15px rgba(0,0,0,0.15);
        }
        .card h3 {
            margin: 10px 0;
            font-size: 20px;
            color: #2f3e46;
        }
        .card p {
            color: #555;
            font-size: 14px;
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
                <img src="Dataset and Database/logo.png" class="header-logo">
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

st.markdown("---")

# Section cards (responsive layout)
st.markdown("### Explore Our Features")

col1, col2, col3 = st.columns(3)

def card(icon, title, description, page):
    if st.markdown(
        f"""
        <div class="card" onclick="window.location.href='/{page}'">
            <h3>{icon} {title}</h3>
            <p>{description}</p>
        </div>
        """,
        unsafe_allow_html=True
    ):
        st.switch_page(f"pages/{page}")

with col1:
    card("📅", "Travel Itinerary", "Plan your complete trip with customizable itineraries.", "travel_itinerary.py")
    card("🤖", "Chat with TravelBot", "Get AI-powered recommendations and answers.", "chatbot.py")

with col2:
    card("☀️", "Check Weather", "Stay informed with real-time weather updates.", "weather.py")
    card("🗺️", "Tourist Guide", "Explore must-visit attractions and hidden gems.", "tourist_guide.py")

with col3:
    card("🏅", "Travel Trivia", "Test your travel knowledge with fun quizzes.", "trivia.py")
    card("🎁", "Souvenirs", "Find and shop for authentic regional souvenirs.", "souvenirs.py")

# Footer
st.markdown("---")
st.write("🚀 Developed with ❤️ for travel enthusiasts")
