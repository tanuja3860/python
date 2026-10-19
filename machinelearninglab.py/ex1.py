from sklearn.linear_model import LinearRegression
import numpy as np

x = np.array([[1], [2], [3], [4], [5]])
y = np.array([3, 5, 7, 9, 11])

model = LinearRegression()
model.fit(x, y)

print(model.predict([[6]]))
Slope = model.coef_[0]
intercept = model.intercept_
print(f"mathematical function:y={Slope:.1f}*x+{intercept:.1f}")