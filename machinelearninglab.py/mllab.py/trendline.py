import matplotlib.pyplot as plt
import numpy as np
# Years of Experience
experience = np.array([2, 3, 4, 5, 5, 7, 8, 9, 10, 12])
# Salary (in Lakhs per annum)
salary = np.array([5, 6, 7, 8, 8,
9, 10, 11, 12, 15])
# Calculate Best Fit Line
m, c = np.polyfit(experience, salary, 1)
# Predicted values on the trend line
trend_line = m * experience + c
plt.figure(figsize=(8,5))
# Scatter Plot
plt.scatter(experience, salary, color='royalblue', s=80, edgecolors='black',label='Employees')
# Trend Line
plt.plot(experience, trend_line, color='red', linewidth=2.5, label='Trend Line' )
plt.title("Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary ( Lakhs per annum)")
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.savefig("trendline.png")
print("trendline saved successfully!")
plt.show()