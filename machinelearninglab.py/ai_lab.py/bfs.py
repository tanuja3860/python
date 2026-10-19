from collections import deque
def bfs_shortest_path(graph, start, goal):
    visited = set()
    queue = deque([[start]])   

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None
graph = {}

n = int(input("Enter the number of vertices: "))

for i in range(n):
    vertex = input(f"\nEnter vertex {i+1}: ")
    neighbors = input(f"Enter neighbors of {vertex} (space-separated): ").split()
    graph[vertex] = neighbors

start = input("\nEnter the starting node: ")
goal = input("Enter the goal node: ")

path = bfs_shortest_path(graph, start, goal)

if path:
    print("\nShortest Path:", " -> ".join(path))
    print("Path Length:", len(path) - 1)
else:
    print("\nNo path exists between", start, "and", goal)