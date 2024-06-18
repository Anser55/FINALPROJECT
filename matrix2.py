print('2')
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sumcolumn = [sum(col) for col in zip(*matrix)]
sumrow = [sum(row) for row in matrix]

print("Sum of columns:", sumcolumn)
print("Sum of rows:", sumrow)