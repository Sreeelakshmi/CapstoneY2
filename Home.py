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
        .section {
            background-color: rgba(255, 255, 255, 0.8);
            padding: 10px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            text-align: center;
        }
        .section img {
            width: 100%;
            border-radius: 10px;
            cursor: pointer;
            transition: transform 0.2s;
        }
        .section img:hover {
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)

# Display logo centered
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.image("Dataset and Database/Eastern Trails.png", use_column_width=True)

# Header section with text
st.markdown('<h1 class="title">Explore the Enchanting North East India</h1>', unsafe_allow_html=True)
st.markdown('<p class="subheader">Your personal travel advisor for the mesmerizing North East</p>', unsafe_allow_html=True)

st.write("---")

# North-East Category Section - Horizontal Scroll with Image Buttons
st.markdown("### Explore By Category")

categories = {
    "Mountains": "https://via.placeholder.com/150?text=Mountains",
    "Tribal Homestays": "https://via.placeholder.com/150?text=Tribal+Homestays",
    "Tea Gardens": "https://via.placeholder.com/150?text=Tea+Gardens",
    "Riverfront Houses": "https://via.placeholder.com/150?text=Riverfront+Houses",
    "Cultural Experiences": "https://via.placeholder.com/150?text=Cultural+Experiences"
}

# Display categories in horizontal layout
category_cols = st.columns(len(categories))

for i, (category, img_url) in enumerate(categories.items()):
    with category_cols[i]:
        st.markdown(f"""
        <div class="section">
            <img src="{img_url}" alt="{category}">
            <p><b>{category}</b></p>
        </div>
        """, unsafe_allow_html=True)

st.write("---")

# Main Feature Sections with Image Buttons
st.markdown("### Discover Our Features")

features = [
    {"name": "Travel Itinerary", "img": "https://via.placeholder.com/150?text=Itinerary", "page": "pages/travel_itenary.py"},
    {"name": "Weather Forecast", "img": "https://via.placeholder.com/150?text=Weather", "page": "pages/weather.py"},
    {"name": "Fun Travel Game", "img": "https://via.placeholder.com/150?text=Game", "page": "pages/game.py"},
    {"name": "Travel Chatbot", "img": "https://via.placeholder.com/150?text=Chatbot", "page": "pages/chatbot.py"},
    {"name": "Souvenirs Guide", "img": "https://via.placeholder.com/150?text=Souvenirs", "page": "pages/souvenirs.py"},
    {"name": "Group Planning", "img": "https://via.placeholder.com/150?text=Group+Planning", "page": "pages/group_planning.py"},
    {"name": "Tourist Guide", "img": "https://via.placeholder.com/150?text=Tourist+Guide", "page": "pages/tourist.py"},
    {"name": "Travel Trivia", "img": "https://via.placeholder.com/150?text=Trivia", "page": "pages/trivia.py"}
]

# 3-column layout for features
cols = st.columns(3)

for idx, feature in enumerate(features):
    with cols[idx % 3]:
        st.markdown(f"""
        <div class="section">
            <a href="{feature['page']}">
                <img src="{feature['img']}" alt="{feature['name']}">
            </a>
            <p><b>{feature['name']}</b></p>
        </div>
        """, unsafe_allow_html=True)

st.write("---")

# Preferences Section with Checkboxes & Progress Bar
st.markdown("### Personalize Your Trip")

preferences = [
    "Mountain Views",
    "Riverfront Stay",
    "Tribal Village Experience",
    "Tea Garden Stay",
    "Cultural Immersion Activities",
    "Eco-Friendly Accommodation",
    "Guided Local Tours",
    "Adventure Activities (Trekking, Rafting)",
    "Organic Local Cuisine"
]

selected_preferences = []
for pref in preferences:
    if st.checkbox(pref):
        selected_preferences.append(pref)

# Progress Bar
progress = len(selected_preferences) / len(preferences)
st.progress(progress)

if selected_preferences:
    st.markdown("#### Your Selected Preferences:")
    st.write(", ".join(selected_preferences))

st.write("---")
st.markdown('<p style="text-align:center; color:#F5F5F5;">Crafted with ❤️ by Eastern Trails - ESTD 2025</p>', unsafe_allow_html=True)

