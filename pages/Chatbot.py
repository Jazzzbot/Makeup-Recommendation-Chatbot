import streamlit as st

def main():
    st.set_page_config(page_title="Chatbot", page_icon="🤖")
    
    st.header("Cosmetics Assistant 🤖")
    
    # Chatbot settings in sidebar
    st.sidebar.subheader("Chatbot Settings")
    bot_persona = st.sidebar.selectbox(
        "Bot Personality",
        ["Professional", "Friendly", "Technical", "Casual"]
    )
    
    # Main chat interface
    st.subheader("Ask me about cosmetics!")
    
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
        
        # Simulate bot response
        with st.chat_message("assistant"):
            response = generate_response(prompt, bot_persona)
            st.markdown(response)
        
        # Add bot response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

def generate_response(prompt, persona):
    """Simple response generator - replace with Rasa integration later"""
    responses = {
        "Professional": [
            "Based on our professional analysis, I recommend...",
            "Our product line includes several options that match your needs..."
        ],
        "Friendly": [
            "Hey there! 😊 I'd suggest trying...",
            "Ooh, great choice! You might love..."
        ],
        # Add more persona-based responses
    }
    
    # Simple keyword matching (replace with actual NLP later)
    if "dry skin" in prompt.lower():
        return f"{responses[persona][0]} products specifically formulated for dry skin."
    elif "price" in prompt.lower():
        return f"{responses[persona][1]} our budget-friendly options starting at $15."
    
    return f"{responses[persona][0]} Please tell me more about your preferences."

if __name__ == "__main__":
    main()