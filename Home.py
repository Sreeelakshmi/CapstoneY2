import os
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Eastern Trails", page_icon="🌄", layout="wide")

# Build the logo path using os.path.join
logo_path = os.path.join("assets", "logo.png")

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
         justify-content: center;
         align-items: center;
         position: relative;
      }
      /* Center the header content but nudge it left */
      .title-container {
         position: absolute;
         left: 20%; /* Adjust this value to move the content toward the left */
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

#########################
# HEADER: Logo & Title  #
#########################
with st.container():
    st.markdown(
        f"""
        <div class="header">
            <div class="title-container">
                <img src="{logo_path}" class="logo">
                <span class="title">Eastern Trails</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# SUBTITLE
st.markdown('<div class="subtitle">Discover the Heart of NorthEast India, One Trail at a Time.</div>', unsafe_allow_html=True)
st.markdown("---")

##############################
# FEATURE CARDS SECTION      #
##############################
st.markdown("### Explore Our Features")

# Define the card data: (Icon, Title, Description, Page filename)
cards = [
    ("📝", "Blog", "Read travel stories and tips.", "blog.py"),
    ("🤖", "Chatbot", "Get AI-powered travel recommendations.", "chatbot.py"),
    ("👥", "Group Planning", "Plan trips with your friends.", "group_planning.py"),
    ("🎁", "Souvenirs", "Find and shop for authentic regional souvenirs.", "souvenirs.py"),
    ("🗺️", "Tourist Guide", "Discover must-visit attractions and hidden gems.", "tourist.py"),
    ("📅", "Travel Itinerary", "Plan your trip with customizable itineraries.", "travel_itinerary.py"),
    ("🏅", "Trivia", "Test your travel knowledge with fun quizzes.", "trivia.py"),
    ("☀️", "Weather", "Stay informed with real-time weather updates.", "weather.py"),
    ("📰", "News", "Get the latest travel news updates.", "news.py"),
]

# Arrange cards in rows of 3 columns
for i in range(0, len(cards), 3):
    cols = st.columns(3)
    for j, col in enumerate(cols):
        idx = i + j
        if idx < len(cards):
            icon, title, description, page = cards[idx]
            button_label = f"{icon} {title}\n\n{description}"
            with col:
                if st.button(button_label, key=title):
                    st.switch_page(f"pages/{page}")

# FOOTER
st.markdown("---")
st.write("🚀 Developed with ❤️ for travel enthusiasts")
