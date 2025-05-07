import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from preprocessing import clean_data  # Make sure preprocessing.py exists

# Configure page
st.set_page_config(page_title="Cosmetics Recommender", layout="wide")

@st.cache_data
def load_data():
    """Load and clean the cosmetics data"""
    df = pd.read_csv("cosmetics.csv")
    df.columns = df.columns.str.lower()  # Standardize column names
    return clean_data(df)  # Apply preprocessing

def data_overview_page(df):
    """Data overview page"""
    st.header("Dataset Overview")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("First 10 rows", df.head(10))
    with col2:
        st.write("Dataset Summary", df.describe())
    
    st.subheader("Missing Values Check")
    st.write(df.isnull().sum())

def visualization_page(df):
    """Data visualization page"""
    st.header("Data Visualizations")
    
    tab1, tab2, tab3 = st.tabs(["Price Analysis", "Skin Type", "Brand Analysis"])
    
    with tab1:
        st.subheader("Price Distribution")
        fig1, ax1 = plt.subplots()
        df["price"].hist(bins=20, ax=ax1)
        ax1.set_xlabel("Price ($)")
        ax1.set_ylabel("Count")
        st.pyplot(fig1)
        
        st.subheader("Price vs Rating")
        fig2, ax2 = plt.subplots()
        sns.scatterplot(data=df, x="price", y="rank", ax=ax2)
        st.pyplot(fig2)
    
    with tab2:
        st.subheader("Products by Skin Type")
        skin_types = ["combination", "dry", "normal", "oily", "sensitive"]
        fig3, ax3 = plt.subplots()
        df[skin_types].sum().plot(kind="bar", ax=ax3)
        st.pyplot(fig3)
    
    with tab3:
        st.subheader("Top Brands by Average Rating")
        top_brands = df.groupby("brand")["rank"].mean().sort_values(ascending=False).head(10)
        st.bar_chart(top_brands)

def chatbot_page():
    """Chatbot interface page"""
    st.header("Cosmetics Assistant")
    st.write("Chatbot functionality will be implemented here")
    # Placeholder for Rasa chatbot integration
    st.text_input("Ask me about cosmetics...", disabled=True)

def main():
    df = load_data()
    
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", 
                           ["Data Overview", "Visualization", "Chatbot"])
    
    if page == "Data Overview":
        data_overview_page(df)
    elif page == "Visualization":
        visualization_page(df)
    elif page == "Chatbot":
        chatbot_page()

if __name__ == "__main__":
    main()
#activate venv using venv\Scripts\activate
#Use streamlit run app.py on terminal(venv) to run on streamlit