import streamlit as st

def main():
    st.set_page_config(page_title="Chatbot", page_icon="🤖")
    
    st.header("Cosmetics Assistant")
    st.write("Chatbot functionality will be implemented here")
    # Rasa chatbot integration here
    st.text_input("Ask me about cosmetics...", disabled=True)

if __name__ == "__main__":
    main()