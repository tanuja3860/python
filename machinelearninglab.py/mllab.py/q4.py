import pandas as pd

df = pd.read_csv("employee.csv")

df["Gender"] = df["Gender"].map({
    "Male": 0,
    "Female": 1
})

print(df)