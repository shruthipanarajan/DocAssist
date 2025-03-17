import pandas as pd

def preprocess_data(input_file, output_file):
    """Function to clean and preprocess the dataset."""

    try:
        print("📂 Loading dataset...")
        df = pd.read_excel(input_file) 
        print("✅ Dataset loaded successfully.")

        # Checking for missing values
        print("\n🔍 Checking for missing values...")
        missing_values = df.isnull().sum()
        print(missing_values[missing_values > 0])

        # Handling missing values
        print("\n🛠️ Handling missing values...")
        for col in df.select_dtypes(include=['number']).columns:  
            df[col].fillna(df[col].mean(), inplace=True)
        print("✅ Missing values handled.")

        # Encoding categorical variables
        print("\n🔄 Encoding categorical variables...")
        df = pd.get_dummies(df, drop_first=True)
        print("✅ Encoding completed.")

        # Saving preprocessed data
        df.to_csv(output_file, index=False)
        print(f"\n✅ Data Preprocessing Completed! Preprocessed data saved at: {output_file}")

    except Exception as e:
        print(f"❌ Error: {e}")

# Run the function
if __name__ == "__main__":
    input_file = "../data/dataset.xlsx"  
    output_file = "../data/preprocessed_data.csv"
    preprocess_data(input_file, output_file)
