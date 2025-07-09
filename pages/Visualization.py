import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from utils.DataLoader import load_data

def main():
    st.set_page_config(page_title="Visualizations", page_icon="📈")
    df = load_data()
    
    st.header("Interactive Data Visualizations")
    
    # Add visualization controls in sidebar
    st.sidebar.subheader("Visualization Controls")
    
    # Price bin control
    bins = st.sidebar.slider(
        "Number of Price Bins",
        min_value=5,
        max_value=50,
        value=20
    )
    
    # Skin type selection
    skin_types = ["combination", "dry", "normal", "oily", "sensitive"]
    selected_skin_types = st.sidebar.multiselect(
        "Select Skin Types",
        options=skin_types,
        default=skin_types
    )
    
    tab1, tab2, tab3 = st.tabs(["Price Analysis", "Skin Type", "Brand Analysis"])
    
    with tab1:
        st.subheader("Price Distribution")
        fig1, ax1 = plt.subplots()
        df["price"].hist(bins=bins, ax=ax1)  # Use dynamic bins
        ax1.set_xlabel("Price ($)")
        ax1.set_ylabel("Count")
        st.pyplot(fig1)
        
        st.subheader("Price vs Rating")
        fig2, ax2 = plt.subplots()
        sns.scatterplot(data=df, x="price", y="rank", ax=ax2)
        st.pyplot(fig2)
        
        # Add correlation threshold slider
        corr_threshold = st.slider(
            "Highlight correlations above:",
            min_value=0.0,
            max_value=1.0,
            value=0.5
        )
        corr = df.select_dtypes(include='number').corr()

        st.write("Correlation Matrix (Highlighted > " + str(corr_threshold) + ")")
        st.dataframe(corr.style.applymap(lambda x: "background-color: yellow" if abs(x) > corr_threshold else ""))
    
    with tab2:
        st.subheader("Products by Skin Type")
        fig3, ax3 = plt.subplots()
        df[selected_skin_types].sum().plot(kind="bar", ax=ax3)  # Use selected skin types
        st.pyplot(fig3)
    
    with tab3:
        st.subheader("Top Brands by Average Rating")
        min_reviews = st.slider(
            "Minimum number of products for brand inclusion",
            min_value=1,
            max_value=50,
            value=5
        )
        brand_stats = df.groupby("brand").agg(
            avg_rating=("rank", "mean"),
            product_count=("rank", "count")
        ).query(f"product_count >= {min_reviews}")
        top_brands = brand_stats.sort_values("avg_rating", ascending=False).head(10)
        st.bar_chart(top_brands["avg_rating"])

if __name__ == "__main__":
    main()