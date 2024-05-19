def floyd(Weight_matrix):
    mat_len = len(Weight_matrix) 
    dist_matrix = [row[:] for row in Weight_matrix]
    
    for intermediate in range(mat_len):
        for start in range(mat_len):
            for dest in range(mat_len):
                dist_matrix[start][dest] = min(dist_matrix[start][dest], dist_matrix[start][intermediate] + dist_matrix[intermediate][dest])
    return dist_matrix

matrix = [
    [0, 3, float('inf'), 5],
    [2, 0, float('inf'), 4],
    [float('inf'), 1, 0, float('inf')],
    [float('inf'), float('inf'), 2, 0]
]

output = floyd(matrix)
for row in output:
    print(row)