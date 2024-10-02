import heapq
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('D', 3)],
    'C': [('D', 1), ('E', 7)],
    'D': [('F', 5)],
    'E': [('F', 3)],
    'F': [] 
}
def uniform_cost_search(graph, start, goal):
    pq = [(0, start, [])] 
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)
        if node in visited:
            continue
        path = path + [node]
        if node == goal:
            return (path, cost)
        visited.add(node)
        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (cost + edge_cost, neighbor, path))

    return None  
start_router = 'A'
destination_router = 'F'
optimal_path, total_cost = uniform_cost_search(graph, start_router, destination_router)
print(f"Optimal Path: {' → '.join(optimal_path)}")
print(f"Total Cost: {total_cost}")