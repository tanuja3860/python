from collections import deque
def monkey_banana_bfs():
    monkey_pos = input("Enter monkey position (Left/Center/UnderBanana): ")
    box_pos = input("Enter box position (Left/Center/UnderBanana): ")
    start_state = (monkey_pos, box_pos, "OnFloor", False)
    queue = deque([(start_state, [("Start", start_state)])])
    visited = {start_state}
    while queue:
        current = queue.popleft()
        state = current[0]
        path = current[1]
        monkey_pos = state[0]
        box_pos = state[1]
        monkey_status = state[2]
        has_banana = state[3]
        if has_banana == True:
            return path
        next_states = []
        if monkey_status == "OnFloor" and monkey_pos != box_pos:
            new_state = (box_pos, box_pos, monkey_status, has_banana)
            next_states.append(("Move to Box", new_state))
        if (monkey_status == "OnFloor" and 
            monkey_pos == box_pos and 
            box_pos != "UnderBanana"):
            new_state = ("UnderBanana", "UnderBanana",
                         monkey_status, has_banana)
            next_states.append(("Push Box under Banana", new_state))
        if monkey_status == "OnFloor" and monkey_pos == box_pos:
            new_state = (monkey_pos, box_pos,
                         "OnBox", has_banana)
            next_states.append(("Climb onto Box", new_state))
        if (monkey_status == "OnBox" and
            box_pos == "UnderBanana" and
            monkey_pos == "UnderBanana"):
            new_state = (monkey_pos, box_pos,
                         monkey_status, True)
            next_states.append(("Grab Banana", new_state))
        for item in next_states:
            action_name = item[0]
            new_state = item[1]
            if new_state not in visited:
                visited.add(new_state)
                queue.append(
                    (new_state, path + [(action_name, new_state)])
                )
    return None
def print_solution(path):
    if path is None:
        print("No solution exists.")
        return
    print("-" * 90)
    print(f"{'Step':<5} {'Action':<25} "
          f"{'Monkey Pos':<15} {'Box Pos':<15} "
          f"{'Status':<12} {'Has Banana'}")
    print("-" * 90)
    step_number = 0
    for item in path:
        action_name = item[0]
        state = item[1]
        monkey_pos = state[0]
        box_pos = state[1]
        monkey_status = state[2]
        has_banana = state[3]
        print(f"{step_number:<5} {action_name:<25} "
              f"{monkey_pos:<15} {box_pos:<15} "
              f"{monkey_status:<12} {str(has_banana)}")
        step_number = step_number + 1
    print("-" * 90)
    print(f"Total steps: {len(path) - 1}")
    print("Goal Achieved: Monkey got the Banana!")
solution_path = monkey_banana_bfs()
print_solution(solution_path)