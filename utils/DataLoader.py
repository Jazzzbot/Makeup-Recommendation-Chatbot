import pandas as pd
from .preprocessing import clean_data
import streamlit as st


@st.cache_data
def load_data():
    df = pd.read_csv("cosmetics.csv")
    df.columns = df.columns.str.strip().str.lower()  # normalize column names
    return df
