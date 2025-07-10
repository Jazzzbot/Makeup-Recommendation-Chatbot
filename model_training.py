import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_squared_error

def train_and_evaluate(df_final):
    # Filter required columns and drop missing data
    df_model = df_final[['Price', 'Label', 'Rank']].dropna()

    X = df_model[['Price', 'Label']]
    y = df_model['Rank']

    # One-hot encode the 'Label' column
    ct = ColumnTransformer([('encoder', OneHotEncoder(), ['Label'])], remainder='passthrough')
    X_transformed = ct.fit_transform(X)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X_transformed, y, test_size=0.2, random_state=42
    )

    # Define models to train
    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
        "Gradient Boosting": GradientBoostingRegressor(random_state=42),
        "Ridge Regression": Ridge(alpha=1.0),
        "Lasso Regression": Lasso(alpha=0.1)
    }

    results = {}

    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        r2 = r2_score(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))

        results[name] = {"R²": r2, "RMSE": rmse}

        print(f"{name}: R² = {r2:.4f}, RMSE = {rmse:.4f}")

    # Save results to CSV
    results_df = pd.DataFrame(results).T
    results_df.to_csv("model_comparison.csv")

    return results
