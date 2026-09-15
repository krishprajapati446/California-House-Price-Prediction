# 🏠 California House Price Prediction

A Machine Learning-based web application that predicts California house prices based on different housing features.

## 📌 Project Overview

This project uses Machine Learning to predict the price of a house based on features such as location, house age, number of rooms, bedrooms, population, households, median income, and ocean proximity.

The trained Machine Learning model is integrated with a Streamlit web application where users can enter housing details and get an estimated house price.

## 🚀 Features

- Predict California house prices
- Interactive Streamlit web interface
- User-friendly input fields
- Machine Learning-based prediction
- Supports different ocean proximity categories
- Displays predicted house price in USD

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

## 📊 Dataset

The project uses the California Housing dataset containing information about California housing districts.

Important features include:

- Longitude
- Latitude
- Housing Median Age
- Total Rooms
- Total Bedrooms
- Population
- Households
- Median Income
- Ocean Proximity

## 🤖 Machine Learning

The project uses a trained Machine Learning model along with a preprocessing pipeline.

The preprocessing pipeline transforms the user input into the required format before passing it to the trained model for prediction.

The trained model and preprocessing pipeline are stored using Joblib as:

- `model.pkl`
- `pipe.pkl`

## 📂 Project Structure

```text
California_House_Prediction/
│
├── app.py
├── main.ipynb
├── housing.csv
├── model.pkl
├── pipe.pkl
├── requirements.txt
└── README.md