import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from faker import Faker
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor


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

df_model = df_final[['Price', 'Label', 'Rank']].dropna()

X = df_model[['Price', 'Label']]
y = df_model['Rank']


ct = ColumnTransformer([('encoder', OneHotEncoder(), ['Label'])], remainder='passthrough')
X_transformed = ct.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=42)


lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)

print("Linear Regression R²:", r2_score(y_test, y_pred_lr))
rmse = np.sqrt(root_mean_squared_error(y_test, y_pred_lr))
print("Linear Regression RMSE:", rmse)


rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

print("Random Forest R²:", r2_score(y_test, y_pred_rf))
rmse2 = np.sqrt(root_mean_squared_error(y_test, y_pred_rf))
print("Random Forest RMSE:", rmse2)

with open("model_results.txt", "w") as f:
    f.write(f"Linear Regression R²: {r2_score(y_test, y_pred_lr)}\n")
    f.write(f"Linear Regression RMSE: {rmse}\n")
    f.write(f"Random Forest R²: {r2_score(y_test, y_pred_rf)}\n")
    f.write(f"Random Forest RMSE: {rmse2}\n")
