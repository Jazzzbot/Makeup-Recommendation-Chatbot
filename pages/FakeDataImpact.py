import streamlit as st
import pandas as pd
from utils.DataLoader import load_data
from fake_data_generator import generate_fake_data
from model_training import train_and_evaluate

def main():
    st.set_page_config(page_title="Fake Data Impact")
    st.header("Impact of Fake Data on Model Performance")

    # Load and display real data
    df_real = load_data()
    st.subheader("Real Dataset")
    st.write("Real Data Size:", df_real.shape)
    st.dataframe(df_real.head())

    # Sidebar control for fake data amount
    st.sidebar.subheader("Fake Data Settings")
    fake_fraction = st.sidebar.slider(
        "Percentage of Fake Data to Add",
        min_value=0.1,
        max_value=0.5,
        value=0.3,
        step=0.05
    )

    # Generate fake data
    df_fake = generate_fake_data(df_real, fraction=fake_fraction)
    df_combined = pd.concat([df_real, df_fake], ignore_index=True)

    # Show sizes
    st.subheader("Generated Fake Data")
    st.write("Fake Data Size:", df_fake.shape)
    st.dataframe(df_fake.head())

    # Train and evaluate on real and combined data
    st.subheader("Model Evaluation")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("** Real Data Only**")
        results_real = train_and_evaluate(df_real)
        st.metric("Linear Reg R²", f"{results_real['lr_r2']:.3f}")
        st.metric("Random Forest R²", f"{results_real['rf_r2']:.3f}")

    with col2:
        st.markdown("** Real + Fake Data**")
        results_combined = train_and_evaluate(df_combined)
        st.metric("Linear Reg R²", f"{results_combined['lr_r2']:.3f}")
        st.metric("Random Forest R²", f"{results_combined['rf_r2']:.3f}")

    # Insight summary
    st.markdown("---")
    
    st.markdown(f"""
    - You added **{int(fake_fraction * 100)}%** fake data.
    
    """)

if __name__ == "__main__":
    main()
