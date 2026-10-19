import heapq
def ucs(graph, start, goal):
    priority_queue = [(0, start, [start])]
    visited = set()
    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            return cost, path
        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                total_cost = cost + edge_cost
                heapq.heappush(
                    priority_queue,
                    (total_cost, neighbor, path + [neighbor])
                )
    return None, None
graph = {}
n = int(input("Enter number of nodes: "))
for i in range(n):
    node = input(f"Enter node {i + 1}: ")
    graph[node] = []
e = int(input("Enter number of edges: "))
for i in range(e):
    u = input("Enter starting node: ")
    v = input("Enter ending node: ")
    cost = int(input("Enter cost: "))
    graph[u].append((v, cost))
start = input("Enter start node: ")
goal = input("Enter goal node: ")
cost, path = ucs(graph, start, goal)
if path:
    print("\nShortest Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("\nNo path found.")