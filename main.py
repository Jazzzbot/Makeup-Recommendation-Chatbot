import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from faker import Faker
import numpy as np

df=pd.read_csv("cosmetics.csv")

sns.boxplot(x=df['Price'])
plt.title("Price Outliers")
plt.show()

Q1 = df["Price"].quantile(0.25)
Q3 = df["Price"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

clean_df = df[(df["Price"] >= lower_bound) & (df["Price"] <= upper_bound)]
print(clean_df)

faker = Faker()
num_fake = int(len(clean_df) * 0.3)

fake_data = []

for _ in range(num_fake):
    fake_data.append({
        'Brand': faker.company(),
        'Name': faker.word(),
        'Label': np.random.choice(clean_df['Label'].dropna().unique()),
        'Price': round(np.random.uniform(5, 100), 2),
        'Rank': round(np.random.uniform(2, 5), 1),
        'Ingredients': faker.words(nb=5)
    })

df_fake = pd.DataFrame(fake_data)

df_final = pd.concat([clean_df, df_fake], ignore_index=True)
df_final.to_csv("cosmetics_with_fake_data.csv", index=False)