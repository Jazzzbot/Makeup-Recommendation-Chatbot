import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from utils.data_loader import load_data

def main():
    st.set_page_config(page_title="Visualizations")
    df = load_data()
    
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

if __name__ == "__main__":
    main()