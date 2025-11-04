import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


data = {
    'Brand': [
        'Maruti', 'Hyundai', 'Tata', 'Mahindra', 'Honda',
        'Toyota', 'Ford', 'Kia', 'Renault', 'Nissan'
    ],
    'Year': [2012, 2015, 2018, 2020, 2017, 2016, 2019, 2021, 2014, 2013],
    'Kms_Driven': [60000, 40000, 35000, 20000, 50000, 45000, 30000, 15000, 70000, 80000],
    'Fuel_Type': ['Petrol', 'Diesel', 'Petrol', 'Diesel', 'Petrol', 'Diesel', 'Petrol', 'Petrol', 'Diesel', 'Petrol'],
    'Transmission': ['Manual', 'Manual', 'Automatic', 'Manual', 'Automatic', 'Manual', 'Manual', 'Automatic', 'Manual', 'Manual'],
    'Owner': ['First Owner', 'Second Owner', 'First Owner', 'First Owner', 'Second Owner', 'First Owner', 'First Owner', 'First Owner', 'Second Owner', 'First Owner'],
    'Selling_Price': [2.8, 4.5, 6.0, 8.5, 5.0, 6.5, 7.2, 9.0, 3.2, 2.5]  # in Lakhs
}

df = pd.DataFrame(data)

df = pd.get_dummies(df, drop_first=True)

X = df.drop('Selling_Price', axis=1)
y = df['Selling_Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

with open("car.pkl", "wb") as f:
    pickle.dump(model, f)

with open("columns.pkl", "wb") as f:
    pickle.dump(list(X.columns), f)

print("✅ car.pkl model created successfully with realistic prices!")