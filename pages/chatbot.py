import pandas as pd
import streamlit as st

# Back to Home Button
if st.button("← Back to Home"):
    st.switch_page("Home")

# The rest of your chatbot.py code below
# (e.g., reading travel package data, defining the chatbot_response function, etc.)

# Dictionary containing general travel information
seven_sisters_info = {
    "Arunachal Pradesh": {
        "History": "Arunachal Pradesh, known as the 'Land of the Rising Sun,' has a rich history influenced by the Monpa Kingdoms, Tibetan culture, and British colonial rule. It became a full-fledged state of India in 1987. The region has historical ties with Tibet and has seen conflicts like the 1962 Indo-China War. The state's history is deeply connected with indigenous tribes and their traditions, including the rule of the Chutia and Ahom dynasties in certain regions.",
        "Best Places": "Tawang Monastery, Ziro Valley, Namdapha National Park, Sela Pass, Bomdila, Itanagar, Mechuka Valley, Dirang, and Pasighat. These locations offer a mix of cultural, spiritual, and adventure experiences, attracting nature lovers and history enthusiasts alike.",
        "Best Time": "October to April is ideal, as the weather is cool and suitable for sightseeing, trekking, and festivals. The monsoon season can make travel difficult due to landslides.",
        "Food": "Apong (rice beer), Thukpa, Zan, Momos, Pika Pila, Bamboo Shoot Dishes, Chura Sabzi, and Marua. Traditional tribal cuisine is heavily influenced by fermented ingredients and locally grown vegetables.",
        "Culture": "A mix of Buddhist, Tibetan, and indigenous tribal traditions. Famous for festivals like Losar, Reh, Si-Donyi, Nyokum, and Solung. The diverse tribal communities celebrate unique rituals and dances.",
        "Travel Options": "Flights to Itanagar, road trips from Assam, and rail connectivity to Naharlagun. [Book on MakeMyTrip](https://www.makemytrip.com/) or [Yatra](https://www.yatra.com/)"
    },
    # ... Other states' info ...
}

# Load travel package data
data_path = 'Dataset and Database/Seven_Sisters_Travel_Packages_Updated.csv'
df = pd.read_csv(data_path)

def fetch_package_info(state, family_friendly=None, budget=None):
    packages = df[df['State'].str.lower() == state.lower()]
    if 'Family_Friendly' in df.columns and family_friendly is not None:
        packages = packages[packages['Family_Friendly'].str.lower() == "yes"] if family_friendly else packages
    if budget is not None and 'Budget(INR)' in df.columns:
        packages = packages[pd.to_numeric(packages['Budget(INR)'], errors='coerce') <= budget]
    return packages.head(1).to_string(index=False) if not packages.empty else "No travel packages available."

def fetch_general_info(state, category=None):
    info = seven_sisters_info.get(state, {})
    return info.get(category, "No information available.") if category else info

def chatbot_response(user_input):
    words = user_input.lower().split()
    for state in seven_sisters_info.keys():
        if state.lower() in words:
            category_map = {
                "history": "History",
                "places": "Best Places",
                "time": "Best Time",
                "food": "Food",
                "culture": "Culture",
                "travel": "Travel Options"
            }
            for key, category in category_map.items():
                if key in words:
                    return f"### 📜 {category} of {state}:\n{fetch_general_info(state, category)}"
            general_info = fetch_general_info(state)
            package_info = fetch_package_info(state)
            return f"### 🏞️ General Information:\n{general_info}\n\n### 📦 Best Travel Packages:\n{package_info}"
    return "Please specify a state from the Seven Sisters of India."

# Streamlit UI
st.set_page_config(page_title="Seven Sisters Travel Chatbot", page_icon="🌍", layout="wide")
st.title("🌏 Seven Sisters Travel Chatbot")
st.markdown("Welcome! Ask me about any Seven Sisters state for travel insights and package details.")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask me about any state from the Seven Sisters!")
if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    response = chatbot_response(user_input)
    st.session_state["messages"].append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)

# Sidebar
st.sidebar.title("🗺️ About the Seven Sisters")
st.sidebar.info("These states are Arunachal Pradesh, Assam, Manipur, Meghalaya, Mizoram, Nagaland, and Tripura.")
st.sidebar.title("📌 How to Use")
st.sidebar.write("1. Type your question in the chat.")

st.sidebar.title("🏝️ Travel Packages")
selected_state = st.sidebar.selectbox("Choose a State", df['State'].unique())
family_friendly = st.sidebar.checkbox("Family Friendly")
budget = st.sidebar.slider("Budget (INR)", min_value=5000, max_value=50000, value=50000)

if selected_state:
    sidebar_package_info = fetch_package_info(selected_state, family_friendly, budget)
    st.sidebar.text_area("Available Packages", sidebar_package_info, height=200)
