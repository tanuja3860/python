import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("employee.csv")

X = df[["Age", "Salary"]]

y = df["Salary"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(X_train)
print(X_test)