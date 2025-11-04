#Used Car Price Predictor

A simple yet powerful *Machine Learning web app* built using *Streamlit* that predicts the selling price of a used car based on its details such as brand, year, kilometers driven, fuel type, transmission, and ownership history.

---

#Project Overview

This project demonstrates how to:
- Train a *Linear Regression* model using a small sample dataset.
- Encode categorical variables using pandas.get_dummies().
- Save and load a trained model using *Pickle (.pkl)*.
- Deploy a beautiful *Streamlit web application* for real-time predictions.



#🧩Tech Stack
| Component | Technology Used |
|------------|----------------|
| Programming Language | Python  |
| Web Framework | Streamlit |
| Machine Learning Model | Linear Regression (Scikit-learn) |
| Libraries | pandas, scikit-learn, pickle, numpy |
| Frontend | Streamlit UI Components |

#📂folder structure
Used_Car/
│
├── train_model.py # Script to train the ML model and save car.pkl
├── used_car_app.py # Streamlit app for user input and prediction
├── car.pkl # Trained Linear Regression model (binary file)
├── columns.pkl # List of feature columns used during training
├── requirements.txt # Dependencies list
└── README.md # Project documentation
