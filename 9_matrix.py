import random

row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))

matrix = [[0 for _ in range(col)] for _ in range(row)]

for i in range(row):
    for j in range(col):
        matrix[i][j] = random.randint(1, 100)
        matrix[j][i] = matrix[i][j]

#print("Matrix:", matrix[0])

print("Matrix:")
for row in matrix:
    print(row)