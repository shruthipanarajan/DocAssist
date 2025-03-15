import joblib
import pandas as pd

# Load trained model
model = joblib.load("D:/Projects/DocAssist/models/final_model.pkl")

# Test with different values
test_cases = [
    {"HAEMATOCRIT": 40.0, "HAEMOGLOBINS": 13.5, "ERYTHROCYTE": 4.5, "LEUCOCYTE": 7.0, "THROMBOCYTE": 250, "MCH": 29.5, "MCHC": 33.5, "MCV": 85.0, "AGE": 30, "SEX": 1},  # Expected: 0
    {"HAEMATOCRIT": 25.0, "HAEMOGLOBINS": 8.5, "ERYTHROCYTE": 3.0, "LEUCOCYTE": 15.0, "THROMBOCYTE": 100, "MCH": 30.0, "MCHC": 33.0, "MCV": 70.0, "AGE": 45, "SEX": 1}, # Expected: 1
]

for case in test_cases:
    df = pd.DataFrame([case])

    # Convert SEX to match training data format
    df["SEX_M"] = df["SEX"].map({1: 1, 0: 0})  # Convert 1->1, 0->0
    df.drop(columns=["SEX"], inplace=True, errors="ignore")  # Drop old column if exists

    probability = model.predict_proba(df)[0][1]  # Get probability of `1`
    prediction = 1 if probability > 0.5 else 0  # Decision threshold

    print(f"📝 Input Data: {case}")
    print(f"🔍 Probability of Treatment Required: {probability:.2f}")
    print(f"📢 Final Prediction: {'Treatment Required' if prediction == 1 else 'No Treatment Needed'}")
    print("-" * 50)
