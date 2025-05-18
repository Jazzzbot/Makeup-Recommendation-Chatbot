import streamlit as st
from utils.data_loader import load_data

def main():
    st.set_page_config(page_title="Data Overview")
    df = load_data()
    
    st.header("Dataset Overview")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("First 10 rows", df.head(10))
    with col2:
        st.write("Dataset Summary", df.describe())
    
    st.subheader("Missing Values Check")
    st.write(df.isnull().sum())

if __name__ == "__main__":
    main()