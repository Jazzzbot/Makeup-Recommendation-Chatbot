import streamlit as st
import pandas as pd
from utils.DataLoader import load_data

def main():
    st.set_page_config(page_title="Data Overview", page_icon="📊")
    df = load_data()
    
    st.header("Dataset Overview")
    
    # Sidebar filters
    st.sidebar.subheader("Filter Data")
    
    selected_brands = st.sidebar.multiselect(
        "Filter by Brand",
        options=df['brand'].unique(),
        default=df['brand'].unique()[:3]
    )
    
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

    # Summary stats block
    st.subheader("Key Statistics")
    col3, col4, col5, col6 = st.columns(4)
    col3.metric("Mean Price", f"${filtered_df['price'].mean():.2f}")
    col4.metric("Max Price", f"${filtered_df['price'].max():.2f}")
    col5.metric("Average Rating", f"{filtered_df['rank'].mean():.2f}")
    col6.metric("Product Count", len(filtered_df))

    # Skin type distribution
    st.subheader("Skin Type Support (Count)")
    skin_cols = ["combination", "dry", "normal", "oily", "sensitive"]
    st.dataframe(filtered_df[skin_cols].sum().sort_values(ascending=False).rename("count"))

    # Missing values
    st.subheader("Missing Values Analysis")
    st.dataframe(filtered_df.isnull().sum())

if __name__ == "__main__":
    main()
