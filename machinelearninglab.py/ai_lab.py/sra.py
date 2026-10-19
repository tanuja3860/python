def simple_reflex_agent(location, status):
    if status == "DIRTY":
        return "SUCK"
    elif location == "A":
        return "MOVE RIGHT"
    elif location == "B":
        return "MOVE LEFT"

def main():
    while True:
        location = input("Enter Room (A/B) or 'exit' to quit: ").upper()

        if location == "EXIT":
            print("Program Ended.")
            break

        status = input("Enter Status (CLEAN/DIRTY): ").upper()

        if location not in ["A", "B"] or status not in ["CLEAN", "DIRTY"]:
            print("Invalid Input! Try Again.\n")
            continue

        action = simple_reflex_agent(location, status)
        print("Action:", action)
        print()

if __name__ == "__main__":
    main()