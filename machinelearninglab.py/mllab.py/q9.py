import pandas as pd

df = pd.read_csv("employee.csv")

df.to_csv("employee_processed.csv", index=False)

print("Processed dataset saved successfully")