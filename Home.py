import streamlit as st

# Set page config
st.set_page_config(page_title="Eastern Trails", page_icon="🌄", layout="wide")

# Load logo image using st.image (works better than img tag for local files)
col_logo, col_title = st.columns([0.15, 0.85])

with col_logo:
    st.image("Dataset and Database/logo.png", width=100)

with col_title:
    st.markdown(
        """
        <h1 style="margin-bottom:0; color:#2f3e46; font-size:36px;">Eastern Trails</h1>
        """,
        unsafe_allow_html=True
    )

# Subtitle
st.markdown("""
### Discover the Heart of NorthEast India, One Trail at a Time.
""")

# Sign In / Sign Up buttons
col_signin, col_signup = st.columns([1, 1])
with col_signin:
    if st.button("Sign In", key="signin"):
        st.write("Sign In clicked!")
with col_signup:
    if st.button("Sign Up", key="signup"):
        st.write("Sign Up clicked!")

st.markdown("---")
st.markdown("### Explore Our Features")

# Feature Section - Using page_link for navigation
col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/travel_itinerary.py", label="📅 Travel Itinerary")
    st.page_link("pages/chatbot.py", label="🤖 Chat with TravelBot")
    st.page_link("pages/trivia.py", label="🏅 Travel Trivia")

with col2:
    st.page_link("pages/weather.py", label="☀️ Check Weather")
    st.page_link("pages/tourist_guide.py", label="🗺️ Tourist Guide")
    st.page_link("pages/souvenirs.py", label="🎁 Souvenirs")

# Footer
st.markdown("---")
st.write("🚀 Developed with ❤️ for travel enthusiasts")
