def agent(percept):
   room, status = percept
   if room == 'A':
       if status == 'CLEAN':
           return 'Move to right'
       elif status == 'DIRTY':
           return 'SUCK'
   elif room == 'B':
       if status == 'CLEAN':
           return 'Move to left'
       elif status == 'DIRTY':
           return 'SUCK'
def main():
   rooms = ['A', 'B']
   clean_status = ['CLEAN', 'DIRTY']
   percept_table = {}  # Dictionary to store percepts and actions
   while True:
       # Prompt user to input room and cleanliness status
       room = input("Enter the room (A/B) or type 'exit' to quit: ")
       if room.lower() == 'exit':
           break
       status = input("Enter the cleanliness status (CLEAN/DIRTY): ")
       # Validate user input
       if room not in rooms or status not in clean_status:
           print("Invalid input!")
           continue
       # Create percept from user input
       percept = (room, status)
       # Call agent function to get action
       action = agent(percept)
       # Store the percept and action in the table
       percept_table[percept] = action
       # Perform action
       print("Action:", action)

   # Print the percept-action table
   print("\nPercept-Action Table:")
   print("---------------------")
   for percept, action in percept_table.items():
       print(f"Percept: {percept}\t\tAction: {action}")
if __name__ == '__main__':
   main()