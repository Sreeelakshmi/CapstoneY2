import streamlit as st

# Set page config
st.set_page_config(page_title="Eastern Trails", page_icon="🌄", layout="wide")

# Custom CSS for a light, Northeast India–inspired theme with enforced styles
st.markdown(
    """
    <style>
      body {
         background-color: #E6F2E6;
      }
      .header {
         background-color: #F5F5DC;
         padding: 15px 20px;
         border-bottom: 2px solid #ddd;
         display: flex;
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
      .subtitle {
         text-align: center;
         font-size: 24px;
         color: #2F3E46;
         margin: 20px 0;
      }
      .card {
         font-size: 16px;
         height: 150px;
         width: 250px;
         background-color: #FFF8E7;
         border: none;
         border-radius: 15px;
         box-shadow: 0 4px 10px rgba(0,0,0,0.1);
         transition: transform 0.3s, box-shadow 0.3s;
         margin-bottom: 20px;
         white-space: pre-line;
         text-align: center;
         display: flex;
         flex-direction: column;
         justify-content: center;
         align-items: center;
         cursor: pointer;
      }
      .card:hover {
         transform: translateY(-5px);
         box-shadow: 0 6px 15px rgba(0,0,0,0.2);
      }
      .card a {
         color: inherit;
         text-decoration: none;
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
        """
        <div class="header">
            <div class="title-container">
                <!-- Updated logo path: assets/logo.png -->
                <img src="assets/logo.png" class="logo">
                <span class="title">Eastern Trails</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
# SUBTITLE
st.markdown('<div class="subtitle">Discover the Heart of NorthEast India, One Trail at a Time.</div>', unsafe_allow_html=True)
st.markdown("---")

st.markdown("### Explore Our Features")

# Define the nine card data: (Icon, Title, Description, Page filename)
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

# Arrange cards in rows of 3 columns using st.columns and custom HTML
for i in range(0, len(cards), 3):
    cols = st.columns(3)
    for j, col in enumerate(cols):
        idx = i + j
        if idx < len(cards):
            icon, title, description, page = cards[idx]
            card_html = f"""
            <div class="card" onclick="window.location.href='pages/{page}'">
                <div style="font-size: 20px;">{icon}</div>
                <div style="font-weight: bold; margin-top: 10px;">{title}</div>
                <div style="font-size: 14px; margin-top: 10px;">{description}</div>
            </div>
            """
            with col:
                st.markdown(card_html, unsafe_allow_html=True)

st.markdown("---")
st.write("🚀 Developed with ❤️ for travel enthusiasts")
