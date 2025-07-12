import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

def train_and_evaluate(df_final):
    df_model = df_final[['price', 'label', 'rank']].dropna()

    X = df_model[['price', 'label']]
    y = df_model['rank']

    ct = ColumnTransformer([('encoder', OneHotEncoder(), ['label'])], remainder='passthrough')
    X_transformed = ct.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=42)

    # Linear Regression
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    y_pred_lr = lr.predict(X_test)
    lr_r2 = r2_score(y_test, y_pred_lr)
    lr_rmse = np.sqrt(mean_squared_error(y_test, y_pred_lr))
    lr_mae = mean_absolute_error(y_test, y_pred_lr)

    # Random Forest
    rf = RandomForestRegressor(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    y_pred_rf = rf.predict(X_test)
    rf_r2 = r2_score(y_test, y_pred_rf)
    rf_rmse = np.sqrt(mean_squared_error(y_test, y_pred_rf))
    rf_mae = mean_absolute_error(y_test, y_pred_rf)

    # Plot comparison
    fig, ax = plt.subplots()
    sns.scatterplot(x=y_test, y=y_pred_lr, label="Linear Reg", ax=ax)
    sns.scatterplot(x=y_test, y=y_pred_rf, label="Random Forest", ax=ax)
    ax.set_xlabel("True Rank")
    ax.set_ylabel("Predicted Rank")
    ax.set_title("Predicted vs Actual Rank")
    ax.legend()

    return {
        "lr_r2": lr_r2,
        "lr_rmse": lr_rmse,
        "lr_mae": lr_mae,
        "rf_r2": rf_r2,
        "rf_rmse": rf_rmse,
        "rf_mae": rf_mae,
        "fig": fig
    }
