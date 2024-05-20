graph = {
    "A": {"B": 3, "D": 4},
    "B": {"A": 3, "C": 1},
    "C": {"D": 2, "B": 1},
    "D": {"C": 2, "A": 4}
}

def prim(graph):
    mst = []
    visited = set()
    start = list(graph.keys())[0]
    
    visited.add(start)
    total_cost = 0
    
    while len(visited) < len(graph):
        min_weight = float('inf')
        min_edge = None
        
        for vertex in visited:
            for adj, weight in graph[vertex].items():
                if adj not in visited and weight < min_weight:
                    min_weight = weight
                    min_edge = (vertex, adj)
                    
        if min_edge:
            visited.add(min_edge[1])
            mst.append((min_edge[0], min_edge[1], min_weight))
            total_cost += min_weight        
            
    return sorted(mst), total_cost


mst, total_cost = prim(graph)

print(f"Minimum Spanning Tree: {mst}")
print(f"Total Cost: {total_cost}")



