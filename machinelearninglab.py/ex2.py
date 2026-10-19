from sklearn.linear_model import LinearRegression
import numpy as np

x = np.array([[2], [4], [6], [8]])
y = np.array([40, 64, 86,95])

model = LinearRegression()
model.fit(x, y)

print(model.predict([[6]]))
Slope = model.coef_[0]
intercept = model.intercept_
print(f"mathematical function:y={Slope:.1f}*x+{intercept:.1f}")