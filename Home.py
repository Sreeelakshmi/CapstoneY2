import streamlit as st

# Set page configuration
st.set_page_config(page_title="Eastern Trails", page_icon="🌄", layout="wide")

# Custom CSS for a light, Northeast India–inspired theme
st.markdown(
    """
    <style>
      /* Overall background */
      body {
        background-color: #E6F2E6;  /* Light earthy green */
      }
      /* Header styling */
      .header {
        background-color: #F5F5DC;  /* Off-white reminiscent of traditional textiles */
        padding: 15px 20px;
        border-bottom: 2px solid #ddd;
        display: flex;
        justify-content: space-between;
        align-items: center;
      }
      .header .title-container {
        display: flex;
        align-items: center;
      }
      .header .logo {
        height: 60px;
      }
      .header .title {
        font-size: 32px;
        font-weight: bold;
        color: #2F3E46;
        margin-left: 15px;
      }
      .header .auth-buttons button {
        margin-left: 10px;
        padding: 8px 15px;
        background-color: #6A994E;  /* Deep natural green */
        color: white;
        border: none;
        border-radius: 20px;
        cursor: pointer;
        font-weight: bold;
      }
      .header .auth-buttons button:hover {
        background-color: #52796F;
      }
      /* Subtitle styling */
      .subtitle {
        text-align: center;
        font-size: 24px;
        color: #2F3E46;
        margin: 20px 0;
      }
      /* Styling for feature cards using Streamlit buttons */
      .stButton>button {
         font-size: 16px;
         height: 150px;
         width: 250px;
         background-color: #FFF8E7;  /* Soft warm cream */
         border: none;
         border-radius: 15px;
         box-shadow: 0 4px 10px rgba(0,0,0,0.1);
         transition: transform 0.3s, box-shadow 0.3s;
         white-space: pre-line;
         text-align: center;
      }
      .stButton>button:hover {
         transform: translateY(-5px);
         box-shadow: 0 6px 15px rgba(0,0,0,0.2);
      }
      /* Grid container for feature cards */
      .card-grid {
         display: flex;
         flex-wrap: wrap;
         justify-content: center;
         gap: 20px;
         margin: 20px;
      }
    </style>
    """,
    unsafe_allow_html=True
)

# HEADER SECTION: Logo, Title, and Auth Buttons
with st.container():
    col_header_left, col_header_right = st.columns([0.7, 0.3])
    with col_header_left:
        st.markdown(
            """
            <div class="title-container">
              <img src="Dataset and Database/eastern_trails_logo.png" class="logo">
              <span class="title">Eastern Trails</span>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col_header_right:
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("Sign In", key="signin"):
                st.info("Sign In clicked!")
        with col_btn2:
            if st.button("Sign Up", key="signup"):
                st.info("Sign Up clicked!")

# SUBTITLE
st.markdown('<div class="subtitle">Discover the Heart of NorthEast India, One Trail at a Time.</div>', unsafe_allow_html=True)
st.markdown("---")

# FEATURE CARDS SECTION
st.markdown("### Explore Our Features")

# Define card data as a list of tuples: (Icon, Title, Description, Page filename)
cards = [
    ("📅", "Travel Itinerary", "Plan your complete trip with customizable itineraries.", "travel_itinerary.py"),
    ("🤖", "Chatbot", "Get AI-powered travel recommendations.", "chatbot.py"),
    ("🏅", "Trivia", "Test your travel knowledge with fun quizzes.", "trivia.py"),
    ("☀️", "Weather", "Stay informed with real-time weather updates.", "weather.py"),
    ("🗺️", "Tourist Guide", "Discover must-visit attractions and hidden gems.", "tourist.py"),
    ("🎁", "Souvenirs", "Find and shop for authentic regional souvenirs.", "souvenirs.py"),
    ("👥", "Group Planning", "Plan trips with your friends.", "group_planning.py"),
    ("📝", "Blog", "Read travel stories and tips.", "blog.py"),
    ("🎮", "Game", "Enjoy interactive travel games.", "game.py")
]

# Arrange cards in a 3x3 grid using a loop with st.columns(3)
for i in range(0, len(cards), 3):
    cols = st.columns(3)
    for j, col in enumerate(cols):
        index = i + j
        if index < len(cards):
            icon, title, description, page = cards[index]
            button_label = f"{icon} {title}\n\n{description}"
            with col:
                if st.button(button_label, key=title, help=f"Go to {title} page"):
                    st.switch_page(f"pages/{page}")

# FOOTER
st.markdown("---")
st.write("🚀 Developed with ❤️ for travel enthusiasts")
