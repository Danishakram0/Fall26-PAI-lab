import pandas as pd
import streamlit as st
import joblib

# Load trained model
model = joblib.load("house_price_model.pkl")

st.title("House Price Prediction App")
st.write("Enter House Details to Predict Price")

# Features same as notebook
inputs = ['OverallQual','GrLivArea','GarageCars','TotalBsmtSF','FullBath','YearBuilt']

input_data = {}

for feature in inputs:
    input_data[feature] = st.number_input(
        f"{feature}",
        value=0.0,
        step=1.0
    )

# Prediction button
if st.button("Predict Price"):

    input_df = pd.DataFrame([input_data])

    prediction = model.predict(input_df)

    st.success(f"Predicted House Price: ${prediction[0]:,.2f}")