import streamlit as st
import pandas as pd
from utils.DataLoader import load_data

def main():
    st.set_page_config(page_title="Product Search", page_icon="🔍")
    st.title("🔍 Product Search")

    df = load_data()

    # Show original column names to let user know what's available
    st.write("Use the filters below to find products.")

    # --- Search bar ---
    search_term = st.text_input("Search by Product Name or Label", "")

    # --- Brand filter ---
    brands = df["brand"].dropna().unique().tolist()
    selected_brands = st.multiselect("Filter by Brand", options=sorted(brands), default=brands)

    # --- Price filter ---
    min_price = float(df["price"].min())
    max_price = float(df["price"].max())
    price_range = st.slider("Price Range ($)", min_value=min_price, max_value=max_price, value=(min_price, max_price))

    # --- Skin type filter ---
    skin_types = ["combination", "dry", "normal", "oily", "sensitive"]
    available_skin_types = [stype for stype in skin_types if stype in df.columns]
    selected_skin_types = st.multiselect("Filter by Skin Type (optional)", options=available_skin_types)

    # --- Filter data ---
    filtered_df = df[
        df["brand"].isin(selected_brands) &
        df["price"].between(price_range[0], price_range[1])
    ]

    if search_term:
        search_term = search_term.lower()
        filtered_df = filtered_df[filtered_df["label"].str.lower().str.contains(search_term)]

    for skin_type in selected_skin_types:
        filtered_df = filtered_df[filtered_df[skin_type] == 1]

    st.write(f"Found {len(filtered_df)} products:")

    if len(filtered_df) > 0:
        st.dataframe(filtered_df.reset_index(drop=True), use_container_width=True)
    else:
        st.info("No products found with the selected filters.")

if __name__ == "__main__":
    main()
