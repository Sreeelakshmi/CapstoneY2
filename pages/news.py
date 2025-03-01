import streamlit as st
import requests

st.title("Travel Advisor News Updates")

@st.cache_data(show_spinner=False)
def fetch_news():
    # Replace with the actual API endpoint from Northeasern news website
    api_url = 'https://api.northeasernnews.com/news'
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        # Assuming the JSON response has an "articles" array
        articles = data.get("articles", [])
        return articles
    except requests.RequestException as e:
        st.error(f"Error fetching news: {e}")
        return []

articles = fetch_news()

if not articles:
    st.info("No news articles available at the moment.")
else:
    for article in articles:
        title = article.get("title", "No Title")
        description = article.get("description", "")
        url = article.get("url", "#")
        image = article.get("image")
        
        # Create a clickable title using Markdown
        st.markdown(f"### [{title}]({url})")
        st.write(description)
        
        if image:
            st.image(image, caption=title, use_column_width=True)
        
        st.markdown("---")
