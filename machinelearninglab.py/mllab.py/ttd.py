import pandas as pd
from sklearn.model_selection import train_test_split
data = {
"Hours":[1,2,3,4,5,6],
"Marks":[30,40,45,60,70,80]
}
df = pd.DataFrame(data)
X = df[["Hours"]]
y = df["Marks"]
X_train, X_test, y_train, y_test = train_test_split(
X,
y,
test_size=0.2,
random_state=42
)
print("Training Data")
print(X_train)
print("Testing Data")
print(X_test)