def mat_add(mat1 , mat2):
    rows = len(mat1)
    cols = len(mat1[0])

    added_mat = []
    for i in range(rows):
        row_list = []
        for j in range(cols):
            row_list.append(0)
        added_mat.append(row_list)

    for i in range(rows):
        for j in range(cols):
            added_mat[i][j] = mat1[i][j] + mat2[i][j]
    return added_mat


rows = int(input('Enter number of rows : '))
columns = int(input('Enter number of columns : '))
mat1 = []
mat2 = []
print('Enter first matrix elements : ')
for i in range(rows):
    row_list = []
    for j in range(columns):
        row_list.append(int(input('Enter a number : ')))
    mat1.append(row_list)
print('Enter second matrix elements : ')
for i in range(rows):
    row_list = []
    for j in range(columns):
        row_list.append(int(input('Enter a number : ')))
    mat2.append(row_list)

print(mat_add(mat1 , mat2))