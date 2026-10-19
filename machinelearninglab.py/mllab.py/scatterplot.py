import matplotlib.pyplot as plt
study_time = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9, 10, 11]
exam_score = [35, 42, 45, 50, 55, 58, 63, 67, 70, 75, 80, 84, 88, 93, 97]
plt.figure(figsize=(8,5))

# Scatter Plot
plt.scatter(
    study_time,
    exam_score,
    color='royalblue',
    edgecolors='black',
    s=80
)

plt.title("Study Time vs Exam Score")
plt.xlabel("Study Time (hours/week)")
plt.ylabel("Exam Score (out of 100)")

plt.xlim(0, 12)
plt.ylim(30, 100)

plt.grid(True, linestyle='--', alpha=0.5)

plt.savefig("scatterplot.png")
print("Scatter plot saved successfully!")

plt.show()