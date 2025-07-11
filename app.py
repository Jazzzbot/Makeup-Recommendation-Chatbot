import streamlit as st
import requests

# Configure the app
st.set_page_config(
    page_title="Cosmetics Recommender",
    page_icon="💄",
    layout="wide"
)

# Sidebar navigation
page = st.sidebar.selectbox("Navigate", ["Home", "Chat with Bot"])

# ---------------- HOME PAGE ----------------
if page == "Home":
    st.markdown("""
    # Welcome to Cosmetics Recommender! 💄

    Navigate to different sections using the sidebar ➡️

    This is a cosmetics recommendation system built for the Assistance Systems project.

    ### 👩‍💻 Team Members
    - Yasaman Hosseini  
    - Sonali Elabada Arachchige (22301094)

    ### 🔍 Features
    - Smart product suggestions based on ingredients
    - Skin-type-based filtering
    - Chatbot interface powered by Rasa

    ### 🚀 Getting Started
    - Head to the **Chat with Bot** section to ask product-related questions!
    """)
    
# ---------------- CHATBOT PAGE ----------------
elif page == "Chat with Bot":
    st.title("💬 Chat with our Skincare Assistant")
    st.markdown("Ask things like:")
    st.markdown("- *What’s the main ingredient in COSRX Snail Mucin?*")
    st.markdown("- *Which products have salicylic acid?*")
    st.markdown("- *What’s good for oily skin?*")

    # Chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous chat messages
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # User input field
    user_input = st.chat_input("Type your question here...")

    if user_input:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Send message to Rasa server
        try:
            response = requests.post(
                "http://localhost:5005/webhooks/rest/webhook",
                json={"sender": "user", "message": user_input}
            )

            bot_reply = "Sorry, I didn't understand that."

            if response.ok:
                messages = response.json()
                if messages:
                    bot_reply = "\n".join([m["text"] for m in messages if "text" in m])

        except Exception as e:
            bot_reply = "Error connecting to Rasa server."

        # Add bot message
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        with st.chat_message("assistant"):
            st.markdown(bot_reply)

#activate venv using venv\Scripts\activate
#Use streamlit run app.py on terminal(venv) to run on streamlit