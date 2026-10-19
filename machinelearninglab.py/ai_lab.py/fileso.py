filename = input("Enter file name: ")

with open(filename, "r") as file:
    data = file.read()

lines = data.splitlines()
words = data.split()
characters = len(data)

print("Number of lines:", len(lines))
print("Number of words:", len(words))
print("Number of characters:", characters)