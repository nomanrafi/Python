# Write a program that can check whether you can perform matrix multiplication on two matrices.

matrix_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
row_1 = 0

for i in matrix_1:
    row_1 = row_1 + 1
    column_1 = len(i)
    print('Matrix_1', i)
print('Row_1', row_1)
print('Column_1', column_1)
matrix_2 = [
    [2, 3],
    [4, 5],
    [7, 8]
]
