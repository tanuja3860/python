import matplotlib.pyplot as plt
data = {
"chocolate": 60,
"strawberry": 40,
"vanalia": 20,
"blackberry": 10
}
plt.figure(figsize=(8,5))
plt.bar(
data.keys(),
data.values(),
color=['brown', 'pink', 'white', 'black'],
edgecolor='black'
)
plt.title("Favorite Programming Language of Students")
plt.xlabel("Programming Language")
plt.ylabel("Number of Students")
plt.grid(axis='y', linestyle='--', alpha=0.5)
for x, y in zip(data.keys(), data.values()):
    plt .text(x, y + 1, str(y), ha='center', fontweight='bold')
plt.show()
plt.savefig("barplot.png")
print("barplot saved successfully!")