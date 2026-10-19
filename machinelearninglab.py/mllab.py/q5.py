import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("employee.csv")

scaler = MinMaxScaler()

df["Salary"] = scaler.fit_transform(df[["Salary"]])

print(df)