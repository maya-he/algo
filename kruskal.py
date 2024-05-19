graph = {
    "A":{"B" : 3,"D" : 4},
    "B":{"A" : 3,"C" : 1},
    'C':{"D" : 2,"B" : 1},
    "D":{"C" : 2,"A" : 4}
}

def kruskal(graph):
    
    edges = []
    for node in graph:
        for adj_node, weight in graph[node].items():
            if (weight, adj_node, node) not in edges:  # Avoid adding duplicate edges
                edges.append((weight, node, adj_node))
    
    edges.sort()
    mst = set()
    parent = {vertex: vertex for vertex in graph}
    total_cost = 0
    
    def find_root(vertex):
        if parent[vertex] != vertex:
            parent[vertex] = find_root(parent[vertex])
        return parent[vertex]
    
    def union(vertex1, vertex2):
        root_v1 = find_root(vertex1)
        root_v2 = find_root(vertex2)
        if root_v1 != root_v2:
            parent[root_v2] = root_v1
        
    for weight, node1, node2 in edges:
        if find_root(node1) != find_root(node2):
            mst.add((weight, node1, node2))
            union(node1,node2)
            total_cost += weight
    return mst, total_cost

minimum_spanning_tree, total_cost = kruskal(graph)

print(f"Minimum Spanning Tree: {minimum_spanning_tree}")
print(f"Total Cost: {total_cost}")
 