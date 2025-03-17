from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load("models/final_model.pkl")  

# Function to preprocess input data
def preprocess_data(data):
    df = pd.DataFrame([data])
    df["SEX_M"] = df["SEX"].map({"M": 1, "F": 0})
    df.drop(columns=["SEX"], inplace=True, errors="ignore")  
    return df

@app.route("/", methods=["GET", "POST"])
def index():
    treatment_recommendation_text = None

    if request.method == "POST":
        # Retrieve form data
        patient_data = {
            "HAEMATOCRIT": float(request.form["HAEMATOCRIT"]),
            "HAEMOGLOBINS": float(request.form["HAEMOGLOBINS"]),
            "ERYTHROCYTE": float(request.form["ERYTHROCYTE"]),
            "LEUCOCYTE": float(request.form["LEUCOCYTE"]),
            "THROMBOCYTE": float(request.form["THROMBOCYTE"]),
            "MCH": float(request.form["MCH"]),
            "MCHC": float(request.form["MCHC"]),
            "MCV": float(request.form["MCV"]),
            "AGE": int(request.form["AGE"]),
            "SEX": request.form["SEX"]
        }

        # Preprocess the data
        processed_data = preprocess_data(patient_data)

        # Get prediction probability
        probability = model.predict_proba(processed_data)[0][1]  # Probability of `1`
        print(f"🔍 DEBUG: Probability of Treatment Required: {probability:.2f}")

        # Lowering the threshold to increase chances of predicting `1`
        treatment_recommendation = 1 if probability > 0.5 else 0  # Change from 0.6 to 0.5
        print(f"📢 DEBUG: Final Prediction = {treatment_recommendation}")


        # Generate text output
        if treatment_recommendation == 1:
            treatment_recommendation_text = "⚠️ Treatment required. Please consult a doctor."
        else:
            treatment_recommendation_text = "✅ No treatment required. Stay healthy!"

    return render_template("index.html", treatment_recommendation=treatment_recommendation_text)

if __name__ == "__main__":
    app.run(debug=True)
