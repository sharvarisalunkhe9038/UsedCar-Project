import streamlit as st
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open("car.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

st.title("🚗 Used Car Price Predictor")
st.markdown("Enter the details below to estimate your car's selling price 💸")

brand = st.selectbox("Select Car Brand", ['Maruti', 'Hyundai', 'Tata', 'Mahindra', 'Honda', 'Toyota', 'Ford', 'Kia', 'Renault', 'Nissan'])
year = st.number_input("Model Year", min_value=2000, max_value=2025)
kms_driven = st.number_input("Kilometers Driven", min_value=0, max_value=300000, value=50000)
fuel = st.selectbox("Fuel Type", ['Petrol', 'Diesel'])
transmission = st.selectbox("Transmission Type", ['Manual', 'Automatic'])
owner = st.selectbox("Ownership", ['First Owner', 'Second Owner'])

input_dict = {
    'Year': year,
    'Kms_Driven': kms_driven,
    'Brand_' + brand: 1,
    'Fuel_Type_' + fuel: 1,
    'Transmission_' + transmission: 1,
    'Owner_' + owner: 1
}


input_df = pd.DataFrame([input_dict])

for col in columns:
    if col not in input_df.columns:
        input_df[col] = 0

input_df = input_df[columns]


if st.button("Predict Price 💰"):
    pred = model.predict(input_df)[0]
    st.success(f"💰 Estimated Price: ₹ {pred * 100000:,.2f}")