j1 = int(input("Enter capacity of Jug 1: "))
j2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))
a = 0
b = 0
print("\nInitial State:", (a, b))
while a != target and b != target:
    if b == 0:
        b = j2
        print("Fill Jug2      :", (a, b))
    elif a == j1:
        a = 0
        print("Empty Jug1     :", (a, b))
    else:
        transfer = min(b, j1 - a)
        a = a + transfer
        b = b - transfer
        print("Pour Jug2->Jug1:", (a, b))
print("\nTarget Reached!")