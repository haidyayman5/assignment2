import heapq
def uniform_cost_search(graph, start, goal):
    queue = [(0, start, [])]

    while queue:
        cost, current, path = heapq.heappop(queue)
        path = path + [current]

        if current == goal:
            return cost, path

        for neighbor, weight in graph.get(current, []):
            heapq.heappush(queue, (cost + weight, neighbor, path))

    return float("inf"), []
graph = {
    'E': [('F', 1), ('G', 4)],
    'F': [('G', 2), ('H', 5)],
    'G': [('H', 1)],
    'H': []}
cost, path = uniform_cost_search(graph, 'E', 'H')
print("Cost:", cost)
print("Path:", path)
