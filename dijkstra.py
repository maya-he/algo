graph = {
    'A': {'D':1, 'B':6},
    'B': {'A':6, 'D':2, 'E':2},
    'C': {'B':5, 'E':5},
    'D': {'A':1, 'E':1, 'B':2},
    'E': {'B':2, 'C':5, 'D':1}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()

    while len(visited) < len(graph):
        min_node = None
        min_distance = float('inf')

        for node in graph:
            if node not in visited and distances[node] < min_distance:
                min_node = node
                min_distance = distances[node]

        visited.add(min_node)

        for neighbor, weight in graph[min_node].items():
            distance = distances[min_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

    return distances



dis = dijkstra(graph,start='A')
print("shortest distances from A ")
for node, distance in dis.items():
    print("to node",node , distance)
