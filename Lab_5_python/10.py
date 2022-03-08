def transpose(matrix):
    a = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            a[j][i] = matrix[i][j]
    for i in range(len(a)):
        for j in range(len(a[0])):
            matrix[i][j] = a[i][j]


matrix = [[1]]
transpose(matrix)
for line in matrix:
    print(*line)

matrix = [[1, 2], [3, 4]]
transpose(matrix)
for line in matrix:
    print(*line)
