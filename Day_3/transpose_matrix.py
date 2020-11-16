def matrix_transpose(matrix):
    print(matrix)
    rows = len(matrix)
    columns = len(matrix[0])
    mat_t = []
    for i in range(columns):
        row_mat = []
        for j in range(rows):
            row_mat.append(0)
        mat_t.append(row_mat)

    for i in range(columns):
        for j in range(rows):
            mat_t[i][j] = matrix[j][i]
    return mat_t

rows = int(input('Enter number of rows : '))
columns = int(input('Enter number of columns : '))
mat = []
for i in range(rows):
    row_list = []
    for j in range(columns):
        row_list.append(int(input('Enter a number : ')))
    mat.append(row_list)

print(matrix_transpose(mat))