import streamlit as st
import requests

# Configure the app
st.set_page_config(
    page_title="Cosmetics Recommender",
    page_icon="💄",
    layout="wide"
)



# ---------------- HOME PAGE ----------------
st.markdown("""
    # Welcome to the Cosmetics Recommender! 💄

    Navigate to different sections using the sidebar ⬅️

    This is a cosmetics recommendation system built for the Assistance Systems project.

    ### 👩‍💻 Team Members
    - Yasaman Hosseini (22300310)
    - Sonali Elabada Arachchige (22301094)

    ### 🔍 Features
    - Smart product suggestions based on ingredients
    - Skin-type-based filtering
    - Chatbot interface powered by Rasa

    ### 🚀 Getting Started
    - Data Overview of the dataset used
    - Our very own Chatbot **Glowbot**  to help find products
    - Fake Data Overview and the impact
    - Models used
    - Visualizations of the data according to price analysis, skin type and brand analysis
    """)
    


#activate venv using venv\Scripts\activate
#Use streamlit run app.py on terminal(venv) to run on streamlit