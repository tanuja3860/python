import matplotlib.pyplot as plt

# Monthly salaries (in thousands)
salaries = [
    52, 55, 56, 58, 60,
    62, 63, 64, 65, 67,
    68, 70, 75, 78,
    80, 83, 87, 120
]

plt.figure(figsize=(8, 5))

# Create Box Plot
plt.boxplot(
    salaries,
    orientation='horizontal',
    patch_artist=True,
    boxprops=dict(facecolor='lightgreen', color='green'),
    medianprops=dict(color='blue', linewidth=2),
    whiskerprops=dict(color='black'),
    capprops=dict(color='black'),
    flierprops=dict(
        marker='o',
        markerfacecolor='red',
        markeredgecolor='red',
        markersize=8
    )
)

plt.title("Monthly Salary Distribution")
plt.xlabel("Salary (in thousands)")
plt.yticks([1], ["Employees"])
plt.grid(axis='x', linestyle='--', alpha=0.5)

# Save the plot
plt.savefig("boxplot.png")
print("Box plot saved successfully!")

# Display the plot
plt.show()