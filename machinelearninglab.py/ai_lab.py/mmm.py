num = sorted(list(map(int, input("Enter numbers: ").split())))
mean = sum(num) / len(num)
n = len(num)
if n % 2 == 0:
    median = (num[n//2 - 1] + num[n//2]) / 2
else:
    median = num[n//2]
mode = num[0]
max_count = 0
for i in num:
    count = num.count(i)
    if count > max_count:
        max_count = count
        mode = i
print("Mean =", mean)
print("Median =", median)
print("Mode =", mode)