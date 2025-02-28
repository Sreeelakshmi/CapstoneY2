import streamlit as st

# Set page config
st.set_page_config(page_title="Eastern Trails", page_icon="🌄", layout="wide")

# Custom CSS for styling with a light theme inspired by NorthEast India
st.markdown(
    """
    <style>
      /* Overall background */
      body {
        background-color: #E6F2E6;  /* Light earthy green */
      }
      /* Header styling */
      .header {
        background-color: #F5F5DC;  /* Off-white, reminiscent of traditional textiles */
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
      /* Card styling */
      .card-link {
        text-decoration: none;
      }
      .card {
        background-color: #FFF8E7;  /* Soft, warm cream */
        width: 250px;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        text-align: center;
        transition: transform 0.3s, box-shadow 0.3s;
        margin-bottom: 20px;
      }
      .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 15px rgba(0,0,0,0.2);
      }
      .card h3 {
        margin: 0;
        font-size: 20px;
        color: #2F3E46;
      }
      .card p {
        margin: 10px 0 0;
        font-size: 14px;
        color: #555;
      }
      /* Grid container for cards */
      .card-grid {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 20px;
      }
    </style>
    """,
    unsafe_allow_html=True
)

# Header Section: Logo, Title, and Auth Buttons
st.markdown(
    """
    <div class="header">
      <div class="title-container">
        <img src="Dataset and Database/eastern_trails_logo.png" class="logo">
        <span class="title">Eastern Trails</span>
      </div>
      <div class="auth-buttons">
        <button onclick="window.location.href='?auth=signin'">Sign In</button>
        <button onclick="window.location.href='?auth=signup'">Sign Up</button>
      </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Subtitle
st.markdown('<div class="subtitle">Discover the Heart of NorthEast India, One Trail at a Time.</div>', unsafe_allow_html=True)
st.markdown("---")

# Function to create a clickable card that opens in the same window
def clickable_card(icon, title, description, page):
    card_html = f"""
    <a class="card-link" href="?page=pages/{page}" target="_self">
      <div class="card">
         <h3>{icon} {title}</h3>
         <p>{description}</p>
      </div>
    </a>
    """
    st.markdown(card_html, unsafe_allow_html=True)

# List of cards (9 total) - arranged in a 3x3 grid
cards = [
    ("📅", "Travel Itinerary", "Plan your complete trip with customizable itineraries.", "travel_itinerary.py"),
    ("🤖", "Chatbot", "Get AI-powered travel recommendations.", "chatbot.py"),
    ("🏅", "Trivia", "Test your travel knowledge with fun quizzes.", "trivia.py"),
    ("☀️", "Weather", "Stay informed with real-time weather updates.", "weather.py"),
    ("🗺️", "Tourist Guide", "Discover must-visit attractions and hidden gems.", "tourist.py"),
    ("🎁", "Souvenirs", "Find and shop for authentic regional souvenirs.", "souvenirs.py"),
    ("👥", "Group Planning", "Plan trips with your friends.", "group_planning.py"),
    ("📝", "Blog", "Read travel stories and tips.", "blog.py"),
]

st.markdown("### Explore Our Features")
st.markdown('<div class="card-grid">', unsafe_allow_html=True)

# Arrange cards in a 3x3 grid
for i in range(0, len(cards), 3):
    cols = st.columns(3)
    for j, col in enumerate(cols):
        index = i + j
        if index < len(cards):
            icon, title, description, page = cards[index]
            with col:
                clickable_card(icon, title, description, page)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.write("🚀 Developed with ❤️ for travel enthusiasts")
