import pandas as pd

data = {
    "Name": ["Ram", "Ravi", "Sita", "Anu", "Kiran"],
    "Age": [22, 24, 21, 23, 25],
    "Gender": ["Male", "Male", "Female", "Female", "Male"],
    "Salary": [25000, 30000, 28000, 35000, 40000]
}

df = pd.DataFrame(data)

df.to_csv("employee.csv", index=False)

print("employee.csv created successfully")