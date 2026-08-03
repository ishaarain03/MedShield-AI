import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# =====================================================
# Page Configuration
# =====================================================

st.set_page_config(
    page_title="MedShield-AI",
    page_icon="🩺",
    layout="wide"
)

# =====================================================
# Load Model
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

model = joblib.load(BASE_DIR / "models" / "heart_disease_model.pkl")
encoders = joblib.load(BASE_DIR / "models" / "encoders.pkl")

# =====================================================
# Title
# =====================================================

st.title("🩺 MedShield-AI")
st.subheader("AI-Powered Heart Disease Prediction System")

st.markdown("---")

st.write("""
Welcome to **MedShield-AI**.

This application predicts the risk of heart disease using Machine Learning.

Developed for research and educational purposes.
""")

st.markdown("## Enter Patient Information")

# =====================================================
# Input Fields
# =====================================================

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=45
    )

    sex = st.selectbox(
        "Sex",
        ["Male", "Female"]
    )



    cp = st.selectbox(
        "Chest Pain Type",
        [
            "typical angina",
            "atypical angina",
            "non-anginal",
            "asymptomatic"
        ]
    )

    trestbps = st.number_input(
        "Resting Blood Pressure",
        80,
        220,
        120
    )

    chol = st.number_input(
        "Cholesterol",
        100,
        600,
        200
    )

    fbs = st.selectbox(
        "Fasting Blood Sugar >120",
        [False, True]
    )

    thal = st.selectbox(
            "Thal",
            [
                "normal",
                "fixed defect",
                "reversable defect"
            ]
        )
    

with col2:

    restecg = st.selectbox(
        "Rest ECG",
        [
            "normal",
            "lv hypertrophy",
            "st-t abnormality"
        ]
    )

    thalch = st.number_input(
        "Maximum Heart Rate",
        60,
        250,
        150
    )

    exang = st.selectbox(
        "Exercise Induced Angina",
        [False, True]
    )

    oldpeak = st.number_input(
        "Oldpeak",
        0.0,
        10.0,
        1.0
    )

    slope = st.selectbox(
        "Slope",
        [
            "upsloping",
            "flat",
            "downsloping"
        ]
    )

    ca = st.number_input(
        "Major Vessels (CA)",
        0.0,
        4.0,
        0.0
    )

# =====================================================
# Prediction
# =====================================================

if st.button("🔍 Predict Heart Disease Risk"):

    try:

        input_data = pd.DataFrame({

            "age": [age],
            "sex": [sex],
            "cp": [cp],
            "trestbps": [trestbps],
            "chol": [chol],
            "fbs": [str(fbs)],
            "restecg": [restecg],
            "thalch": [thalch],
            "exang": [str(exang)],
            "oldpeak": [oldpeak],
            "slope": [slope],
            "ca": [ca],
            "thal": [thal]

        })

        categorical_columns = [
            "sex",
            "cp",
            "fbs",
            "restecg",
            "exang",
            "slope",
            "thal"
        ]

        for col in categorical_columns:
            input_data[col] = encoders[col].transform(
                input_data[col].astype(str)
            )

        prediction = model.predict(input_data)
        probability = model.predict_proba(input_data)

        st.markdown("---")

        # =====================================================
        # Prediction Result
        # =====================================================

        if prediction[0] == 0:

            st.markdown("""
### 🟢 Low Risk Detected

Your prediction indicates a low likelihood of heart disease.
""")

            st.info("""
### Recommendation

✔ Maintain a healthy lifestyle.

✔ Exercise regularly.

✔ Eat a balanced diet.

✔ Schedule regular health checkups.
""")

        else:

            st.error("## ⚠️ HIGH RISK")

            st.warning("""
### Recommendation

⚠ Please consult a cardiologist.

⚠ Maintain a healthy diet.

⚠ Avoid smoking and alcohol.

⚠ Regular monitoring is recommended.
""")

        # =====================================================
        # Prediction Probability
        # =====================================================

        st.markdown("---")
        st.subheader("📊 Prediction Probability")

        low = probability[0][0] * 100
        high = probability[0][1] * 100

        st.progress(float(max(low, high) / 100))

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "🟢 Low Risk",
                f"{low:.2f}%"
            )

        with col2:
            st.metric(
                "🔴 High Risk",
                f"{high:.2f}%"
            )

        # =====================================================
        # Patient Summary
        # =====================================================

        st.markdown("---")
        st.subheader("👤 Patient Summary")

        summary = pd.DataFrame({

            "Feature": [

                "Age",
                "Sex",
                "Chest Pain",
                "Blood Pressure",
                "Cholesterol",
                "Fasting Blood Sugar",
                "Rest ECG",
                "Maximum Heart Rate",
                "Exercise Angina",
                "Oldpeak",
                "Slope",
                "Major Vessels (CA)",
                "Thal"

            ],

            "Value": [
               
                age,
                sex,
                cp,
                trestbps,
                chol,
                fbs,
                restecg,
                thalch,
                exang,
                oldpeak,
                slope,
                ca,
                thal

            ]

        })

        st.dataframe(
    summary,
    use_container_width=True,
    hide_index=True
)

    except Exception as e:

        st.error(f"Prediction Error:\n\n{e}")