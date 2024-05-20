def Warshall(adj_matrix):
    matrix_len = len(adj_matrix)
    R_matrix = [row[:] for row in adj_matrix]
    
    for intermediate in range(matrix_len):
        for vertex1 in range(matrix_len):
            for vertex2 in range(matrix_len):
                R_matrix[vertex1][vertex2] = R_matrix[vertex1][vertex2] or R_matrix[vertex1][intermediate] and R_matrix[intermediate][vertex2]
                
    return R_matrix

adjacency_matrix = [
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 0, 0]
]

transitive_closure = Warshall(adjacency_matrix)

print("Reachability matrix:")
for row in transitive_closure:
    print(row)