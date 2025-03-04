from sklearn.linear_model import LinearRegression
import numpy as np

energy_input = np.array([50, 60, 70, 80, 90]).reshape(-1, 1)
hydrogen_output = np.array([0.8, 1.0, 1.2, 1.4, 1.6])


model = LinearRegression()
model.fit(energy_input, hydrogen_output)

predicted_output = model.predict([[100]])
print(f"Predicted Hydrogen Output: {predicted_output[0]:.2f} kg")
