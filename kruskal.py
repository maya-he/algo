graph = {
    'A': {'B': 4, 'C': 4},
    'B': {'A': 4, 'C': 2},
    'C': {'A': 4, 'B': 2, 'D': 3, 'E': 2, 'F': 4},
    'D': {'C': 3, 'F': 3},
    'E': {'C': 2, 'F': 3},
    'F': {'D': 3, 'C': 4, 'E': 3}
}


def kruskal(graph):

    edges = []
    for u in graph:
        for v, weight in graph[u].items():
            edges.append((weight, u, v))

    edges.sort()
    mst = set()
    parent = {vertex: vertex for vertex in graph}           #{A:A, B:A , ...}
    total_cost = 0

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_y] = root_x

    for weight, u, v in edges:
        if find(u) != find(v):
            mst.add((u, v, weight))
            union(u, v)
            total_cost += weight
    return mst, total_cost


minimum_spanning_tree, total_cost = kruskal(graph)
print("Minimum Spanning Tree:", minimum_spanning_tree)
print("Total Cost:", total_cost)
