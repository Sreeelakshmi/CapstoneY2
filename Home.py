import streamlit as st

def main():
    # Airbnb-style header
    st.markdown(
        """
        <style>
            .header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 10px 30px;
                border-bottom: 1px solid #ddd;
                font-family: Arial, sans-serif;
            }
            .header-logo {
                color: #FF5A5F;
                font-weight: bold;
                font-size: 24px;
            }
            .header-nav a {
                margin-left: 20px;
                font-weight: bold;
                color: #333;
                text-decoration: none;
            }
            .progress-bar {
                width: 100%;
                height: 8px;
                background-color: #eee;
                border-radius: 4px;
                margin: 15px 0;
                overflow: hidden;
            }
            .progress {
                height: 100%;
                background-color: #FF5A5F;
                width: 0%;
                transition: width 0.3s ease;
            }
            .checkbox-item {
                margin: 8px 0;
            }
        </style>
        <div class="header">
            <div class="header-logo">airbnb</div>
            <div class="header-nav">
                <a href="#">Stays</a>
                <a href="#">Experiences</a>
                <a href="#">Airbnb your home</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.title("Trip Preferences")

    st.write("### Select your preferences:")

    # Checkbox options
    options = {
        "Hotel booked": st.checkbox("Hotel booked"),
        "Transportation booked": st.checkbox("Transportation booked"),
        "Activities planned": st.checkbox("Activities planned"),
        "Travel insurance purchased": st.checkbox("Travel insurance purchased")
    }

    # Progress bar calculation
    completed = sum(options.values())
    total = len(options)
    progress_percentage = (completed / total) * 100

    # Display progress bar
    st.markdown(f"""
        <div class="progress-bar">
            <div class="progress" style="width: {progress_percentage}%"></div>
        </div>
        <p>{progress_percentage:.0f}% completed</p>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
