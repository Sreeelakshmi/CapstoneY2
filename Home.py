import streamlit as st

st.set_page_config(page_title="Travel Advisor Home", page_icon="🌍")

st.title("🌍 Welcome to Travel Advisor")

st.write("Explore various tools and features to make your travel planning fun and easy!")

st.header("Explore Sections:")

if st.button("📅 Travel Itinerary"):
    st.switch_page("pages/travel_itenary.py")

if st.button("🌦️ Weather Forecast"):
    st.switch_page("pages/weather.py")

if st.button("💬 Chatbot Assistant"):
    st.switch_page("pages/chatbot.py")

if st.button("❓ Trivia Game"):
    st.switch_page("pages/trivia.py")

if st.button("🗺️ Tourist Guide"):
    st.switch_page("pages/tourist.py")

if st.button("🎁 Souvenirs"):
    st.switch_page("pages/souvenirs.py")

if st.button("🧩 Group Planning"):
    st.switch_page("pages/group_planning.py")

if st.button("🎮 Travel Game"):
    st.switch_page("pages/game.py")

st.write("---")
st.write("Made with ❤️ using Streamlit")

