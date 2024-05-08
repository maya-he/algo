def warshall_algorithm(adjacency_matrix):
    n = len(adjacency_matrix)
    R = [row[:] for row in adjacency_matrix]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                R[i][j] = R[i][j] or (R[i][k] and R[k][j])

    return R

adjacency_matrix = [
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 0, 0]
]

transitive_closure = warshall_algorithm(adjacency_matrix)
for row in transitive_closure:
    print(row)
