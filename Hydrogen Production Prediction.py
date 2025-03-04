from sklearn.linear_model import LinearRegression
import numpy as np

# Data: Energy input (kWh) vs. Hydrogen output (kg)
energy_input = np.array([50, 60, 70, 80, 90]).reshape(-1, 1)
hydrogen_output = np.array([0.8, 1.0, 1.2, 1.4, 1.6])

# Train model
model = LinearRegression()
model.fit(energy_input, hydrogen_output)

# Predict hydrogen output for 100 kWh
predicted_output = model.predict([[100]])
print(f"Predicted Hydrogen Output: {predicted_output[0]:.2f} kg")