import streamlit as st

# Set page config
st.set_page_config(page_title="Eastern Trails", page_icon="🌄", layout="wide")

# Custom CSS for styling with a light, Northeast India–inspired theme
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
        justify-content: flex-start;
        align-items: center;
      }
      .title-container {
        display: flex;
        align-items: center;
      }
      .logo {
        height: 60px;
      }
      .title {
        font-size: 32px;
        font-weight: bold;
        color: #2F3E46;
        margin-left: 15px;
      }
      /* Subtitle styling */
      .subtitle {
        text-align: center;
        font-size: 24px;
        color: #2F3E46;
        margin: 20px 0;
      }
      /* Styling for Streamlit buttons as cards */
      .stButton>button {
         font-size: 16px;
         height: 150px;
         width: 250px;
         background-color: #FFF8E7;  /* Soft warm cream */
         border: none;
         border-radius: 15px;
         box-shadow: 0 4px 10px rgba(0,0,0,0.1);
         transition: transform 0.3s, box-shadow 0.3s;
         margin-bottom: 20px;
         white-space: pre-line;
         text-align: center;
      }
      .stButton>button:hover {
         transform: translateY(-5px);
         box-shadow: 0 6px 15px rgba(0,0,0,0.2);
      }
    </style>
    """,
    unsafe_allow_html=True
)

##############################
# HEADER: Logo & Title Only #
##############################
with st.container():
    # Create a single row for the header
    st.markdown(
        """
        <div class="header">
            <div class="title-container">
                <img src="Dataset and Database/eastern_trails_logo.png" class="logo">
                <span class="title">Eastern Trails</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# SUBTITLE
st.markdown('<div class="subtitle">Discover the Heart of NorthEast India, One Trail at a Time.</div>', unsafe_allow_html=True)
st.markdown("---")

############################################
# Feature Cards (Including Sign In/Sign Up)#
############################################
st.markdown("### Explore Our Features")

# Card data: (Icon, Title, Description, Key)
# For "Sign In" and "Sign Up", we won't do page navigation; we'll just show a message.
cards = [
    ("🔑", "Sign In", "Access your account or manage your trips.", "signin"),
    ("🆕", "Sign Up", "Create a new account to plan your adventures!", "signup"),
    ("📅", "Travel Itinerary", "Plan your trip with customizable itineraries.", "travel_itinerary.py"),
    ("🤖", "Chatbot", "Get AI-powered travel recommendations.", "chatbot.py"),
    ("🏅", "Trivia", "Test your travel knowledge with fun quizzes.", "trivia.py"),
    ("☀️", "Weather", "Stay informed with real-time weather updates.", "weather.py"),
    ("🗺️", "Tourist Guide", "Discover must-visit attractions and hidden gems.", "tourist.py"),
    ("🎁", "Souvenirs", "Find and shop for authentic regional souvenirs.", "souvenirs.py"),
    ("👥", "Group Planning", "Plan trips with your friends.", "group_planning.py"),
    ("📝", "Blog", "Read travel stories and tips.", "blog.py"),
    ("🎮", "Game", "Enjoy interactive travel games.", "game.py"),
]

# We'll arrange them in rows of 3 columns each
for i in range(0, len(cards), 3):
    cols = st.columns(3)
    for j, col in enumerate(cols):
        idx = i + j
        if idx < len(cards):
            icon, title, description, page_key = cards[idx]
            # Multiline label for the card
            button_label = f"{icon} {title}\n\n{description}"
            with col:
                # If it's "Sign In" or "Sign Up", show an info message, else switch page
                if st.button(button_label, key=title):
                    if page_key == "signin":
                        st.info("Sign In clicked!")
                    elif page_key == "signup":
                        st.info("Sign Up clicked!")
                    else:
                        st.switch_page(f"pages/{page_key}")

# FOOTER
st.markdown("---")
st.write("🚀 Developed with ❤️ for travel enthusiasts")
