import streamlit as st

# Set page config
st.set_page_config(page_title="Eastern Trails", page_icon="🌄", layout="wide")

# Custom CSS for styling
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
        background-color: #6A994E;  /* Deep, natural green */
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
      /* Card container */
      .card-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 20px;
        margin: 20px;
      }
      /* Card styling */
      .card {
        background-color: #FFF8E7;  /* Soft, warm cream */
        width: 250px;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        text-align: center;
        transition: transform 0.3s, box-shadow 0.3s;
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
      a.card-link {
        text-decoration: none;
      }
    </style>
    """,
    unsafe_allow_html=True
)

# Header Section
st.markdown(
    """
    <div class="header">
      <div class="title-container">
        <img src="Dataset and Database/logo.png" class="logo">
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

# Function to create a clickable card
def clickable_card(icon, title, description, page):
    # The href uses Streamlit's multipage routing format:
    #   /?page=pages/<filename>
    card_html = f"""
    <a class="card-link" href="/?page=pages/{page}">
      <div class="card">
         <h3>{icon} {title}</h3>
         <p>{description}</p>
      </div>
    </a>
    """
    st.markdown(card_html, unsafe_allow_html=True)

# Cards Section
st.markdown("### Explore Our Features")
st.markdown('<div class="card-container">', unsafe_allow_html=True)

clickable_card("📅", "Travel Itinerary", "Plan your complete trip with customizable itineraries.", "travel_itinerary.py")
clickable_card("🤖", "Chatbot", "Get AI-powered travel recommendations.", "chatbot.py")
clickable_card("🏅", "Trivia", "Test your travel knowledge with fun quizzes.", "trivia.py")
clickable_card("☀️", "Weather", "Stay informed with real-time weather updates.", "weather.py")
clickable_card("🗺️", "Tourist Guide", "Discover must-visit attractions and hidden gems.", "tourist.py")
clickable_card("🎁", "Souvenirs", "Find and shop for authentic regional souvenirs.", "souvenirs.py")
clickable_card("👥", "Group Planning", "Plan trips with your friends.", "group_planning.py")
clickable_card("📝", "Blog", "Read travel stories and tips.", "blog.py")
clickable_card("🎮", "Game", "Enjoy interactive travel games.", "game.py")

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.write("🚀 Developed with ❤️ for travel enthusiasts")
