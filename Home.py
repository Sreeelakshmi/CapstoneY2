import streamlit as st

# Set page config
st.set_page_config(page_title="Eastern Trails", layout="wide")

# Set custom styles for North East India theme
st.markdown(
    """
    <style>
        body {
            background-color: #1B4332;
            color: #F5F5DC;
            font-family: 'Arial', sans-serif;
        }
        .block-container {
            background-color: #1B4332;
            padding: 20px;
            border-radius: 10px;
        }
        .nav-button {
            display: inline-block;
            padding: 8px 15px;
            margin: 5px;
            background-color: #8B0000;
            color: #FFFFFF;
            border: 1px solid #F5F5DC;
            border-radius: 20px;
            text-transform: uppercase;
            font-weight: bold;
            text-align: center;
            cursor: pointer;
        }
        .nav-button:hover {
            background-color: #B22222;
        }
        .search-bar {
            display: flex;
            justify-content: center;
            align-items: center;
            background: #F5F5DC;
            padding: 10px;
            border-radius: 30px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
            margin: 20px 0;
        }
        .search-input {
            flex: 1;
            padding: 10px;
            border: none;
            border-right: 1px solid #ddd;
            outline: none;
            background: white;
        }
        .search-button {
            padding: 10px 20px;
            background-color: #8B0000;
            color: white;
            border: none;
            border-radius: 30px;
            cursor: pointer;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #F5F5DC;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Header Section (with Eastern Trails Logo)
header_col1, header_col2, header_col3 = st.columns([1, 3, 1])

with header_col1:
    st.image("Dataset and Database/Eastern Trails.png", width=120)

with header_col2:
    st.markdown(
        """
        <div style="text-align: center;">
            <span class="nav-button">BLOG</span>
            <span class="nav-button">CHATBOT</span>
            <span class="nav-button">GROUP PLANNING</span>
            <span class="nav-button">SOUVENIRS</span>
            <span class="nav-button">TOURIST</span>
            <span class="nav-button">TRAVEL ITINERARY</span>
            <span class="nav-button">TRIVIA</span>
            <span class="nav-button">WEATHER</span>
        </div>
        """,
        unsafe_allow_html=True
    )

with header_col3:
    st.write("")

st.write("---")

# Search Bar Section (Airbnb style but North East themed)
st.markdown(
    """
    <div class="search-bar">
        <input class="search-input" type="text" placeholder="Where - Search destinations">
        <input class="search-input" type="text" placeholder="Check in - Add dates">
        <input class="search-input" type="text" placeholder="Check out - Add dates">
        <input class="search-input" type="text" placeholder="Who - Add guests">
        <button class="search-button">🔍</button>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("---")

# Travel Preferences Section
st.header("Travel Preferences Progress")

options = [
    "Hotel Booked",
    "Transportation Booked",
    "Activities Planned",
    "Travel Insurance Purchased",
    "Documents Ready"
]

progress = 0
total_options = len(options)

for option in options:
    if st.checkbox(option, key=option):
        progress += 1

progress_percentage = (progress / total_options) * 100
st.progress(progress_percentage / 100)

st.write(f"### Progress: {progress} of {total_options} completed")
