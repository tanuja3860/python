import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split

# Creating the dataset
df = pd.DataFrame({
    "Name": ["A", "B", "C", "D", "E"],
    "Age": [22, 25, 21, 24, 23],
    "Gender": ["Male", "Female", "Male", "Female", "Male"],
    "Salary": [20000, 25000, 30000, 35000, 40000],
    "Experience": [1, 2, 3, 4, 5]
})

# Savind  and read CSV
df.to_csv("employee.csv", index=False)
df = pd.read_csv("employee.csv")

# First five records
print(df.head())

# Missing values
df.loc[1, "Salary"] = None
df.loc[3, "Salary"] = None
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Encode Gender
df["Gender"] = df["Gender"].map({"Male": 0, "Female": 1})

# Normalize Salary
scaler = MinMaxScaler()
df["Salary"] = scaler.fit_transform(df[["Salary"]])

# Standardize Age
std = StandardScaler()
df["Age"] = std.fit_transform(df[["Age"]])

# Train-Test Split
X = df[["Age", "Salary"]]
y = df["Experience"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))

# Save processed dataset
df.to_csv("employee_processed.csv", index=False)

print("Processed dataset saved successfully.")