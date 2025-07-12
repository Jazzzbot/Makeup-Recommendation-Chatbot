from data_cleaning import load_and_clean_data
from fake_data_generator import generate_fake_data
from from_sklearn import train_and_evaluate
import pandas as pd

def main():
    # Load and prepare data
    clean_df = load_and_clean_data("cosmetics.csv")
    df_fake = generate_fake_data(clean_df)
    
    df_final = pd.concat([clean_df, df_fake], ignore_index=True)
    df_final.to_csv("cosmetics_with_fake_data.csv", index=False)

    # Train models and evaluate
    results = train_and_evaluate(df_final)  

    # Print all model results
    print("\n Model Performance Summary:")
    for model_name, metrics in results.items():
        print(f"{model_name}: R² = {metrics['R²']:.4f}, RMSE = {metrics['RMSE']:.4f}")

    # Save to text file
    with open("model_results.txt", "w") as f:
        f.write("Model Performance Summary:\n")
        for model_name, metrics in results.items():
            f.write(f"{model_name}: R² = {metrics['R²']:.4f}, RMSE = {metrics['RMSE']:.4f}\n")

    print("\n Results saved to 'model_results.txt' and 'model_comparison.csv'.")

if __name__ == "__main__":
    main()
