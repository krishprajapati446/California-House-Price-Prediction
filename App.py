import streamlit as st
import joblib 
import pandas as pd
import sklearn

st.title("California House Price Prediction")

longitude = st.number_input("Longitude")
latitude = st.number_input("Latitude")
house_age = st.number_input("House age")
total_rooms = st.number_input("Total rooms")
total_bedrooms = st.number_input("Total bedrooms")
population = st.number_input("Population")
households = st.number_input("Households")
income = st.number_input("Median income")


ocean = st.selectbox(
    "Ocean proximity",
    [
        "<1H OCEAN",
        "INLAND",
        "ISLAND",
        "NEAR BAY",
        "NEAR OCEAN"
    ]
)


model = joblib.load("model.pkl")
pipeline = joblib.load("pipe.pkl")

# Prediction Button

if st.button("Predict Price"):
    input_df = pd.DataFrame({
        "longitude" : [longitude],
        "latitude" : [latitude],
        "housing_median_age" : [house_age],
        "total_rooms" : [total_rooms],
        "total_bedrooms" : [total_bedrooms],
        "population" : [population],
        "households" : [households],
        "median_income" : [income],
        "ocean_proximity" : [ocean]
    })   
    
    input_transformed = pipeline.transform(input_df)
    
    prediction = model.predict(input_transformed)
    
    st.success(f"Predicted House Price : ${prediction[0]:,.2f}")
    

