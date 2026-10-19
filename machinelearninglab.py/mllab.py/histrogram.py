import matplotlib.pyplot as plt

scores = [
    43, 52,54, 55, 56, 59, 61,
    64, 68, 71, 73, 74, 78,79,
    81, 85, 89, 92, 100
]

bins = [40, 50, 60, 70, 80, 90, 100]

plt.figure(figsize=(8, 5))
plt.hist(scores, bins=bins, edgecolor='black', color='steelblue')

plt.title("Distribution of Test Scores")
plt.xlabel("Score Intervals")
plt.ylabel("Frequency (No. of Students)")
plt.xticks([40, 50, 60, 70, 80, 90, 100])
plt.grid(axis='y', linestyle='--', alpha=0.3)

plt.show()
plt.savefig("histogram.png")
print("Histogram saved successfully!")