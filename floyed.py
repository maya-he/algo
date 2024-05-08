def floyd_algorithm(W):
    n = len(W)
    D = [row[:] for row in W]  

    for k in range(n):      
        for i in range(n):
            for j in range(n):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])

    return D

A = [
    [0, 3, float('inf'), 5],
    [2, 0, float('inf'), 4],
    [float('inf'), 1, 0, float('inf')],
    [float('inf'), float('inf'), 2, 0]
]

result = floyd_algorithm(A)
for row in result:
    print(row)
