import streamlit as st

# Set page config
st.set_page_config(page_title="Eastern Trails", layout="wide")

# Set custom styles for North East India theme with lighter colors and darker text
st.markdown(
    """
    <style>
        body {
            background-color: #E6F2E6;  /* Light earthy green */
            color: #1F2E24;  /* Dark green text */
            font-family: 'Arial', sans-serif;
        }
        .block-container {
            background-color: #E6F2E6;
            padding: 20px;
            border-radius: 10px;
        }
        .nav-button {
            display: inline-block;
            padding: 8px 15px;
            margin: 5px;
            background-color: #79AC78; /* Soft green */
            color: #FFFFFF;
            border: 1px solid #2E3D34;
            border-radius: 20px;
            text-transform: uppercase;
            font-weight: bold;
            text-align: center;
            cursor: pointer;
        }
        .nav-button:hover {
            background-color: #618264;
        }
        h1, h2, h3, h4, h5, h6, p, label {
            color: #1F2E24; /* Darker text for readability */
        }
        .scrollable-container {
            max-height: 80vh;
            overflow-y: auto;
            padding: 15px;
            background-color: #FFFFFF;
            border: 1px solid #79AC78;
            border-radius: 10px;
        }
        .action-button {
            display: inline-block;
            padding: 10px 20px;
            margin: 5px;
            background-color: #618264;
            color: #FFFFFF;
            font-weight: bold;
            border: none;
            border-radius: 20px;
            cursor: pointer;
        }
        .action-button:hover {
            background-color: #4E6B4F;
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

# Scrollable Content Section
st.markdown('<div class="scrollable-container">', unsafe_allow_html=True)

# Travel Preferences Buttons (Replacing the Checklist)
st.header("Travel Preferences")

buttons = [
    "Hotel Booked",
    "Transportation Booked",
    "Activities Planned",
    "Travel Insurance Purchased",
    "Documents Ready"
]

button_html = "".join([f'<button class="action-button">{button}</button>' for button in buttons])

st.markdown(f'<div style="text-align: center;">{button_html}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
