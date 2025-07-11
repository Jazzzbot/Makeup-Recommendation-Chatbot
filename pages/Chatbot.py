import streamlit as st
import requests

RASA_URL = "http://localhost:5005/webhooks/rest/webhook"  # Make sure your Rasa server runs here

def main():
    st.set_page_config(page_title="Chatbot", page_icon="🤖")

    st.header("Cosmetics Assistant 🤖")

    # Chatbot settings in sidebar
    st.sidebar.subheader("Chatbot Settings")
    bot_persona = st.sidebar.selectbox(
        "Bot Personality",
        ["Professional", "Friendly", "Technical", "Casual"]
    )

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("What cosmetics are you looking for?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # Send user message to Rasa and get response
        with st.chat_message("assistant"):
            response = ask_rasa(prompt)
            st.markdown(response)

        # Add bot response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})


def ask_rasa(message: str) -> str:
    """Send message to Rasa REST webhook and return the bot's reply."""
    try:
        payload = {"sender": "user", "message": message}
        response = requests.post(RASA_URL, json=payload)
        response.raise_for_status()
        messages = response.json()  # List of dicts with 'text' keys
        bot_replies = [msg.get("text", "") for msg in messages]
        return "\n".join(bot_replies) if bot_replies else "Sorry, I didn't get that."
    except Exception as e:
        return f"Error communicating with Glambot: {e}"

if __name__ == "__main__":
    main()
