import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("employee.csv")

scaler = StandardScaler()

df["Age"] = scaler.fit_transform(df[["Age"]])

print(df)