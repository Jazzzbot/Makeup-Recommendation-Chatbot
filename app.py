import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("cosmetics.csv")
    
    # Correct way 1: Create a figure first
    st.header("Method 1: Explicit Figure")
    fig, ax = plt.subplots()
    df["Price"].hist(bins=20, ax=ax)
    st.pyplot(fig)
    
    # Correct way 2: Use pandas plotting with get_figure()
    st.header("Method 2: get_figure()")
    ax = df["Price"].hist(bins=20)
    st.pyplot(ax.get_figure())
    
    # Correct way 3: Use st.bar_chart for simple histograms
    st.header("Method 3: Streamlit native")
    st.bar_chart(df["Price"].value_counts(bins=20))

if __name__ == "__main__":
    main()
#activate venv using venv\Scripts\activate
#Use streamlit run app.py on terminal(venv) to run on streamlit