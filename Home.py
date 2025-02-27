import streamlit as st

# Set full-page config
st.set_page_config(page_title="Eastern Trails", layout="wide")

# Apply global page style (full green background and dark text)
st.markdown(
    """
    <style>
        body {
            background-color: #E6F2E6; /* Full-page light green */
        }
        .block-container {
            background-color: #E6F2E6; /* Keep background consistent */
            padding: 20px;
            border-radius: 10px;
        }
        h1, h2, h3, h4, h5, h6, p, label {
            color: #1F2E24; /* Dark green text */
            font-family: Arial, sans-serif;
        }
        .travel-button {
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
        .travel-button:hover {
            background-color: #4E6B4F;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Header Section with Text (instead of buttons)
col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    st.image("Dataset and Database/Eastern Trails.png", width=120)

with col2:
    st.markdown(
        """
        <div style="text-align: center;">
            <h2>Welcome to Eastern Trails!</h2>
            <p>Explore the untouched beauty of North East India. Plan your perfect trip with our tools and guides.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.write("")  # Empty space

st.write("---")

# Travel Preferences Section
st.header("Travel Preferences")

# Travel Preference Buttons
buttons = [
    "Hotel Booked",
    "Transportation Booked",
    "Activities Planned",
    "Travel Insurance Purchased",
    "Documents Ready"
]

button_html = "".join([f'<button class="travel-button">{button}</button>' for button in buttons])

st.markdown(f'<div style="text-align: center;">{button_html}</div>', unsafe_allow_html=True)
