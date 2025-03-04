import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import streamlit as st

# Load data (replace with actual data)
data = pd.read_csv('biofuel_data.csv')

# Preprocessing
X = data[['crop_type', 'residue_availability', 'temperature', 'humidity', 'water_availability']]
y = data['biofuel_yield']

# One-hot encode categorical data
X = pd.get_dummies(X, columns=['crop_type'], drop_first=True)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

