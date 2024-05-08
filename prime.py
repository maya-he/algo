graph = {
    'A' : {'C':4, 'B':4},
    'B' : {'A':4, 'C':2},
    'C' : {'A':4, 'B':2, 'D':3, 'E':2, 'F':4},
    'E' : {'C':2, 'F':3} ,
    'D' : {'C':3, 'F':3},
    'F' : {'E':3, 'D':3, 'C':4}
}

def prime(graph):
    mst = set()
    start = list(graph.keys())[0]
    mst.add(start)
    total_cost = 0

    while len(mst) < len(graph):
        min_weight = float('inf')
        min_edge = None

        for vertex in mst:
            for neighbor, weight in graph[vertex].items():
                if neighbor not in mst and weight < min_weight:
                    min_weight = weight
                    min_edge = (vertex, neighbor)

        if min_edge:
            mst.add(min_edge[1]) 
            total_cost += min_weight

    return sorted(mst), total_cost

print(prime(graph))




