def simple_reflex_agent(floor, room, status):
    if status == "DIRTY":
        return "SUCK"
    else:
        if room == "A":
            return "MOVE TO ROOM B"
        elif room == "B":
            if floor == 1:
                return "MOVE TO FLOOR 2 ROOM A"
            else:
                return "MOVE TO FLOOR 1 ROOM A"

def main():
    while True:
        floor = input("Enter Floor (1/2) or 'exit' to quit: ")

        if floor.lower() == "exit":
            print("Program Ended.")
            break

        floor = int(input(floor))
        room = input("Enter Room (A/B): ").upper()
        status = input("Enter Status (CLEAN/DIRTY): ").upper()

        if floor not in [1, 2] or room not in ["A", "B"] or status not in ["CLEAN", "DIRTY"]:
            print("Invalid Input! Try Again.\n")
            continue

        action = simple_reflex_agent(floor, room, status)
        print("Action:", action)
        print()

if __name__ == "__main__":
    main()