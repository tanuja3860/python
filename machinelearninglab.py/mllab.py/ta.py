from sklearn.semi_supervised import LabelSpreading
import numpy as np
X = np.array([[1, 2],[1.5, 1.8],[5, 6],[4.8, 5.2]])
y = np.array([0, -1, 1, -1])
model = LabelSpreading()
model.fit(X, y)
print("Semi-Supervised Propagated Labels:", model.transduction_)
print("\n--- Propagated Data Breakdown ---")
for i, (features, final_label) in enumerate(zip(X, model.transduction_)):
    original = "Unlabeled -> " if y[i] == -1 else "Originally Labeled -> "
    print(f"Item {i+1} {features}: {original}Final Label: {final_label}")
