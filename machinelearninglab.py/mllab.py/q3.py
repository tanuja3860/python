import pandas as pd

df = pd.read_csv("employee.csv")

df.loc[1, "Salary"] = None
df.loc[3, "Salary"] = None

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print(df)