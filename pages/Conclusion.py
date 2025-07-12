import streamlit as st

def main():
    st.set_page_config(page_title="Conclusion", page_icon="✅")
    st.title("✅ Conclusion and Reflection")

    st.markdown("## 📌 Project Summary")
    st.write("""
    This project focused on analyzing cosmetic product data to build regression models that predict product ranking based on features like price and label.
    The objective was to explore how different model types perform on real-world e-commerce data, and to present results through an interactive Streamlit app.
    """)

    st.markdown("## 🤖 Models Compared")
    st.markdown("""
    - **Linear Regression**
      - Simple and interpretable baseline model.
    - **Random Forest**
      - Ensemble method that captured non-linear relationships better.
    
    We evaluated each model using:
    - R² Score
    - RMSE (Root Mean Squared Error)
    """)

    st.markdown("## 📊 Key Results")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Best R² Score", "0.82", delta="Random Forest")
    with col2:
        st.metric("Lowest RMSE", "1.73", delta="Random Forest")

    st.markdown("## 🔍 Insights")
    st.markdown("""
    - **Price** had some influence on product rank, but not linearly.
    - **Label/Brand** contributed meaningfully when one-hot encoded.
    - Random Forest outperformed Linear Regression in all metrics.

    This suggests the relationships between features and product rankings are non-linear and potentially complex.
    """)

    st.markdown("## 🚀 Future Improvements")
    st.markdown("""
    - Use more product metadata (ingredients, reviews).
    - Try deep learning (e.g., neural networks) for better generalization.
    - Use NLP to extract features from product descriptions.
    - Improve data quality by filtering out fake or noisy entries.
    """)

    st.markdown("## 🧠 Final Thoughts")
    st.success("Building this pipeline and dashboard provided valuable experience in model training, evaluation, and visualization. It also highlighted the importance of clean, meaningful data when developing machine learning systems.")

if __name__ == "__main__":
    main()
