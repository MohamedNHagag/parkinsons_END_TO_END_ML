import streamlit as st
import numpy as np
import pandas as pd
from src.components.utils import load_object
from src.exception import CustomException
import sys
import os


# Load model and preprocessor
model_path = os.path.join("artificial", "ModelParkinsons.pkl")
preprocessor_path = os.path.join("artificial", "Transformation", "preprocessor.pkl")

model = load_object(model_path)
preprocessor = load_object(preprocessor_path)

# Page title
st.title("🧠 Parkinson's Disease Prediction")

st.write("Enter the following values to predict:")
# Input fields
def user_input():
    feature_names = [
        'MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)',
        'MDVP:Jitter(Abs)', 'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer',
        'MDVP:Shimmer(dB)', 'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA',
        'NHR', 'HNR', 'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE'
    ]

    inputs = []
    for name in feature_names:
        value = st.number_input(name, value=0.0)
        inputs.append(value)

    return np.array(inputs).reshape(1, -1)


input_data = user_input()
# Button to predict
if st.button("🔍 Predict"):
    try:
        input_scaled = preprocessor.transform(input_data)
        prediction = model.predict(input_scaled)

        if prediction[0] == 1:
            st.error("❌ The person is likely to have Parkinson's Disease.")
        else:
            st.success("✅ The person is not likely to have Parkinson's Disease.")
    except Exception as e:
        raise CustomException(e, sys)
