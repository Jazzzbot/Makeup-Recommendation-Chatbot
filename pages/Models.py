import streamlit as st
from utils.DataLoader import load_data
from model_training import train_and_evaluate

def main():
    st.set_page_config(page_title="Model Evaluation", page_icon="🤖")
    st.title("📊 Model Results & Comparison")

    df = load_data()

    with st.sidebar:
        st.header("Model Controls")
        run_lr = st.checkbox("Run Linear Regression", value=True)
        run_rf = st.checkbox("Run Random Forest", value=True)
        show_plot = st.checkbox("Show Prediction Plot", value=True)
        st.markdown("---")
        show_info = st.checkbox("Show Model Description")

    if not run_lr and not run_rf:
        st.warning("Please select at least one model to run.")
        return

    results = train_and_evaluate(df)

    tabs = []
    if run_lr:
        tabs.append("Linear Regression")
    if run_rf:
        tabs.append("Random Forest")

    selected_tab = st.radio("Select Model Results", tabs)

    if selected_tab == "Linear Regression":
        st.subheader("🔹 Linear Regression Metrics")
        col1, col2, col3 = st.columns(3)
        col1.metric("R²", f"{results['lr_r2']:.3f}")
        col2.metric("RMSE", f"{results['lr_rmse']:.3f}")
        col3.metric("MAE", f"{results['lr_mae']:.3f}")

    if selected_tab == "Random Forest":
        st.subheader("🌲 Random Forest Metrics")
        col4, col5, col6 = st.columns(3)
        col4.metric("R²", f"{results['rf_r2']:.3f}")
        col5.metric("RMSE", f"{results['rf_rmse']:.3f}")
        col6.metric("MAE", f"{results['rf_mae']:.3f}")

    if show_plot:
        st.subheader("📈 Prediction Comparison Plot")
        st.pyplot(results["fig"])

    if show_info:
        with st.expander("ℹ️ Model Descriptions"):
            st.markdown("""
            - **Linear Regression** assumes a linear relationship between input features and target.
            - **Random Forest** builds multiple decision trees and averages their predictions.
            - **R² (Coefficient of Determination)** shows variance explained.
            - **RMSE** shows average prediction error (in units).
            - **MAE** shows absolute error (less sensitive to outliers).
            """)

if __name__ == "__main__":
    main()
