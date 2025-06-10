import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)

    sns.boxplot(x=df['Price'])
    plt.title("Price Outliers")
    plt.show()

    Q1 = df["Price"].quantile(0.25)
    Q3 = df["Price"].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    clean_df = df[(df["Price"] >= lower_bound) & (df["Price"] <= upper_bound)]
    return clean_df
