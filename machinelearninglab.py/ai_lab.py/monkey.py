def move(location):
    print(f"Monkey moves to the {location}.")

def push_box(destination):
    print(f"Monkey pushes the box to the {destination}.")

def climb_box():
    print("Monkey climbs onto the box.")

def take_banana():
    print("Monkey takes the banana.")
    print("\nGoal Achieved: Monkey has the banana!")
monkey = input("Enter Monkey Position (Door/Window/Center): ").lower()
box = input("Enter Box Position (Door/Window/Center): ").lower()
banana = input("Enter Banana Position (Door/Window/Center): ").lower()

print("\nExecution Steps:")

if monkey != box:
    move(box)
    monkey = box


if box != banana:
    push_box(banana)
    box = banana
    monkey = banana


climb_box()

if monkey == banana:
    take_banana()
else:
    print("Monkey cannot reach the banana.")