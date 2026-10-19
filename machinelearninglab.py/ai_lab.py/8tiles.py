import heapq
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
def heuristic(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            x, y = divmod(i, 3)
            gx, gy = divmod(state[i] - 1, 3)
            distance += abs(x - gx) + abs(y - gy)
    return distance
def solve(start):
    pq = []
    heapq.heappush(pq, (heuristic(start), 0, start, []))
    visited = set()
    while pq:
        f, g, state, path = heapq.heappop(pq)
        if state in visited:
            continue
        visited.add(state)
        if state == goal:
            return path + [state]
        zero = state.index(0)
        row, col = divmod(zero, 3)
        moves = []
        if row > 0:
            moves.append(zero - 3)
        if row < 2:
            moves.append(zero + 3)
        if col > 0:
            moves.append(zero - 1)
        if col < 2:
            moves.append(zero + 1)
        for pos in moves:
            new_state = list(state)
            new_state[zero], new_state[pos] = new_state[pos], new_state[zero]
            new_state = tuple(new_state)
            if new_state not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(new_state)
                heapq.heappush(
                    pq, (new_f, new_g, new_state, path + [state])
                )
    return None
print("Enter the initial state (use 0 for blank):")
start = tuple(map(int, input().split()))
solution = solve(start)
if solution:
    print("\nSolution:")
    for state in solution:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()
    print("Number of moves:", len(solution) - 1)
else:
    print("No solution found.")