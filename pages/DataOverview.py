import streamlit as st
import pandas as pd
from utils.data_loader import load_data

def main():
    st.set_page_config(page_title="Data Overview", page_icon="📊")
    df = load_data()
    
    st.header("Dataset Overview")
    
    # Add filtering widgets
    st.sidebar.subheader("Filter Data")
    
    # Brand multi-select
    selected_brands = st.sidebar.multiselect(
        "Filter by Brand",
        options=df['brand'].unique(),
        default=df['brand'].unique()[:3]
    )
    
    # Price range slider
    price_range = st.sidebar.slider(
        "Price Range ($)",
        float(df['price'].min()),
        float(df['price'].max()),
        (float(df['price'].min()), float(df['price'].max()))
    )
    
    # Apply filters
    filtered_df = df[
        (df['brand'].isin(selected_brands)) &
        (df['price'] >= price_range[0]) & 
        (df['price'] <= price_range[1])
    ]
    
    # Display filtered data
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"Filtered Data ({len(filtered_df)} rows)", filtered_df.head(10))
    with col2:
        st.write("Filtered Summary", filtered_df.describe())
    
    # Missing values analysis
    st.subheader("Missing Values Analysis")
    st.write(filtered_df.isnull().sum())

if __name__ == "__main__":
    main()