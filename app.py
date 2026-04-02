from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("diabetes_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    features = np.array([
        data["weight"],
        data["height"],
        data["blood_glucose"],
        data["physical_activity"],
        data["diet"],
        data["medical_adherence"],
        data["stress_level"],
        data["sleep_hour"],
        data["hydration_level"],
        data["bmi"]
    ]).reshape(1,-1)

    prediction = model.predict(features)[0]

    return jsonify({
        "risk_score": round(prediction,2)
    })

if __name__ == "__main__":
    app.run(debug=True)