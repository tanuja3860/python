
num = list(map(int, input("Enter numbers : ").split()))
even = []
odd = []
for i in num:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbers:", even)
print("Odd numbers:", odd)