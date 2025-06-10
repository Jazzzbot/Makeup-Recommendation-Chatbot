from data_cleaning import load_and_clean_data
from fake_data_generator import generate_fake_data
from model_training import train_and_evaluate
import pandas as pd

def main():
    clean_df = load_and_clean_data("cosmetics.csv")
    df_fake = generate_fake_data(clean_df)
    
    df_final = pd.concat([clean_df, df_fake], ignore_index=True)
    df_final.to_csv("cosmetics_with_fake_data.csv", index=False)

    results = train_and_evaluate(df_final)

    print("Linear Regression R²:", results['lr_r2'])
    print("Linear Regression RMSE:", results['lr_rmse'])
    print("Random Forest R²:", results['rf_r2'])
    print("Random Forest RMSE:", results['rf_rmse'])

    with open("model_results.txt", "w") as f:
        f.write(f"Linear Regression R²: {results['lr_r2']}\n")
        f.write(f"Linear Regression RMSE: {results['lr_rmse']}\n")
        f.write(f"Random Forest R²: {results['rf_r2']}\n")
        f.write(f"Random Forest RMSE: {results['rf_rmse']}\n")

if __name__ == "__main__":
    main()
