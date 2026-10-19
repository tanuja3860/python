from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
X_train = np.array([[1000], [1500], [2000], [2500], [3000]])
y_train = np.array([1200, 1700, 2100, 2600, 3100])
model = LinearRegression()
model.fit(X_train, y_train)
X_test = np.array([[1200], [1800], [2200], [2800]])
y_true = np.array([1400, 1950, 2300, 2850])
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_true, y_pred)
mse = mean_squared_error(y_true, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_true, y_pred)
print("--- House Rent Predictions ---")
for size, true, pred in zip(X_test.flatten(), y_true, y_pred):
    print(f"Size: {size} sq ft -> Actual Rent: ${true} | Predicted Rent: ${pred:.2f}")
print("\n--- Regression Performance Measures ---")
print(f"Mean Absolute Error (MAE): ${mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): ${rmse:.2f}")
print(f"R-squared (R² Score): {r2:.4f} ({r2:.2%})")