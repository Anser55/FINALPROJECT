matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
transposed_matrix1 = [[matrix1[j][i] for j in range(len(matrix1))] for i in range(len(matrix1[0]))]
transposed_matrix2 = [[matrix2[j][i] for j in range(len(matrix2))] for i in range(len(matrix2[0]))]


print("Transposed Matrix 1:")
for row in transposed_matrix1:
    print(row)

print("\nTransposed Matrix 2:")
for row in transposed_matrix2:
    print(row)

print("Transposed Matrix 1:")
for row in transposed_matrix1:
    print(row)

print("\nTransposed Matrix 2:")
for row in transposed_matrix2:
    print(row)
print("Transposed Matrix 1:")
for row in transposed_matrix1:
    print(row)

print("\nTransposed Matrix 2:")
for row in transposed_matrix2:
    print(row)