import pandas as pd
import seaborn as sn

df = pd.read_csv("cosmetics.csv")

def clean_data(input_df):
    """Clean the input DataFrame"""
    df = input_df.copy()
    # cleaning code here
    return df

print(df.isnull().sum())  # Any missing data?
print(df.describe())      # Check min/max price, ratings
clean_df = clean_data(df)
