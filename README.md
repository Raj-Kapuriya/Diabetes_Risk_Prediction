<div align="center">

# 🩺 Diabetes Risk Predictor
### AI-Powered Health Risk Assessment Tool

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-black?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4.0-orange?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<br/>

> **Enter your health metrics and get an instant AI-powered diabetes risk score — right in your browser, 100% locally.**

<br/>

![Diabetes Risk Predictor Preview](static/bg.png)

</div>

---

## ✨ Features

- 🤖 **ML-Powered Prediction** — Tuned Gradient Boosting model gives accurate real-time risk scores.
- ⚡ **Instant Results** — No page reload; results appear instantly via async API.
- 🔒 **100% Local & Private** — All data stays on your machine, nothing is sent to any cloud.
- 🎨 **Premium Dark UI** — Animated diabetes-themed floating background with a glassmorphism card.
- 📱 **Fully Responsive** — Works beautifully on desktop and mobile browsers.
- ✅ **Smart Validation** — Highlights missing or invalid fields before prediction.

---

## 🔬 Machine Learning Model

This project doesn't just use a basic model; it utilizes an optimized **Gradient Boosting Regressor** to predict the diabetes risk score with high accuracy. 

Detailed implementation can be found in [`Diabetes.ipynb`](Diabetes.ipynb).

### 1. Data Preparation
- The dataset (`diabetes_data.csv`) contains 1,000 synthetic patient records.
- **Features Extracted:** `weight`, `height`, `blood_glucose`, `physical_activity`, `diet`, `medication_adherence`, `stress_level`, `sleep_hours`, `hydration_level`, `bmi`.
- **Target Variable:** `risk_score`

### 2. Model Selection & Comparison
Two models were initially evaluated on an 80/20 train-test split:
- **Random Forest Regressor:** Achieved an $R^2$ score of `0.904` and a Cross-Validation score of `0.892`.
- **Gradient Boosting Regressor:** Achieved a superior $R^2$ score of **`0.978`** and a Cross-Validation score of **`0.975`**.

Due to its superior performance, **Gradient Boosting** was selected as the final algorithm.

### 3. Hyperparameter Tuning
To squeeze out even more performance, we utilized `RandomizedSearchCV` to find the optimal parameters across:
- `n_estimators`: [50, 100, 150]
- `learning_rate`: [0.01, 0.5, 0.1]
- `max_depth`: [4, 5, 6]

**Best Parameters Found:**
```python
GradientBoostingRegressor(n_estimators=50, learning_rate=0.5, max_depth=4)
```

### 4. Feature Importance
Based on the tree-based model's feature importance analysis, the most critical features driving the diabetes risk score are:
1. **BMI** (~35.4% importance)
2. **Physical Activity** (~23.2% importance)
3. **Blood Glucose** (~15.9% importance)
4. **Diet** (~10.9% importance)

### 5. Final Export
The tuned Gradient Boosting model was exported using `joblib` into `diabetes_model.pkl`, which is loaded directly by the Flask API for real-time inference.

---

## 🖥️ User Interface

| Input | Result |
|-------|--------|
| Fill in 10 health metrics | Instant risk score (0–1) |
| ✅ Low Risk `< 0.4` | 🟢 Green indicator |
| ⚠️ Moderate Risk `0.4–0.7` | 🟡 Yellow indicator |
| 🚨 High Risk `> 0.7` | 🔴 Red indicator |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip

### 1. Clone the Repository

```bash
git clone https://github.com/Raj-Kapuriya/Diabetes_Risk_Prediction.git
cd Diabetes_Risk_Prediction
```

### 2. Create a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
python app.py
```

Then open your browser at **http://127.0.0.1:5000** 🎉

---

## 📁 Project Structure

```
Diabetes_Risk_Prediction/
│
├── app.py                  # Flask backend & prediction API
├── diabetes_model.pkl      # Pre-trained Gradient Boosting ML model
├── requirements.txt        # Python dependencies
├── Diabetes.ipynb          # Model training, EDA, and tuning notebook
│
├── Templates/
│   └── index.html          # Main frontend page
│
└── static/
    ├── style.css           # Premium CSS with animations
    └── bg.png              # Diabetes-themed floating background
```

---

## 🔌 API Reference

### `POST /predict`

Accepts a JSON body with 10 health features and returns a risk score.

**Request:**
```json
{
  "weight": 75,
  "height": 170,
  "bmi": 25.9,
  "blood_glucose": 130,
  "physical_activity": 2,
  "sleep_hour": 6,
  "stress_level": 2,
  "diet": 0,
  "medical_adherence": 1,
  "hydration_level": 0
}
```

**Response:**
```json
{
  "risk_score": 0.82
}
```

---

## ⚠️ Disclaimer

> This tool is for **informational and educational purposes only**.
> It is **not a substitute** for professional medical advice, diagnosis, or treatment.
> Always consult a qualified healthcare professional for any health concerns.

---

## 👤 Author

**Raj Kapuriya**

[![GitHub](https://img.shields.io/badge/GitHub-Raj--Kapuriya-181717?style=flat-square&logo=github)](https://github.com/Raj-Kapuriya)

---

<div align="center">

Made with ❤️ and Python &nbsp;|&nbsp; ⭐ Star this repo if you found it helpful!

</div>
