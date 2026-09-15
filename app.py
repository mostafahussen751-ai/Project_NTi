import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("diabetes_model.pkl")

st.title("Diabetes Prediction App")

st.write("Enter the patient information:")

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

age = st.number_input(
    "Age",
    min_value=0.0,
    max_value=120.0,
    value=50.0
)

hypertension = st.selectbox(
    "Hypertension",
    [0, 1]
)

heart_disease = st.selectbox(
    "Heart Disease",
    [0, 1]
)

smoking_history = st.selectbox(
    "Smoking History",
    ["never", "No Info", "current", "former", "ever", "not current"]
)

bmi = st.number_input(
    "BMI",
    min_value=0.0,
    max_value=100.0,
    value=25.0
)

HbA1c_level = st.number_input(
    "HbA1c Level",
    min_value=0.0,
    max_value=20.0,
    value=5.5
)

blood_glucose_level = st.number_input(
    "Blood Glucose Level",
    min_value=0,
    max_value=500,
    value=100
)

if st.button("Predict"):

    input_data = pd.DataFrame({
        "gender": [gender],
        "age": [age],
        "hypertension": [hypertension],
        "heart_disease": [heart_disease],
        "smoking_history": [smoking_history],
        "bmi": [bmi],
        "HbA1c_level": [HbA1c_level],
        "blood_glucose_level": [blood_glucose_level]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("The model predicts Diabetes.")
    else:
        st.success("The model predicts No Diabetes.")