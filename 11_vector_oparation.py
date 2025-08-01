import random

rows = int (input("Enter the number of rows: "))
cols = int (input("Enter the number of columns: "))

#initialzing the 2D list
A = [[random.randint(10, 100) for _ in range (cols)] for _ in range (rows)]
B = [[random.randint(10, 100) for _ in range (cols)] for _ in range (rows)]

print(" matix A is: ")
for row in A:
    print(row)

print(" matix B is: ")
for row in B:
    print(row)

rows_A = len(A)
cols_A = len(A[0])
c = 5
d = 10
line_AB = [[0 for _ in range(cols)] for _ in range(rows)]
if rows_A == len(B) and cols_A == len(B[0]):
    print(" Linear Combination of A and B is:")
    for i in range (rows):
        for j in range (cols):
            line_AB [i][j] = c*A[i][j] + d*B[i][j]
else:
    print("It can't wright as a Linear Combination.")

for row in line_AB:
    print(row)

   #Vector multiplecation
vector = [random.randint(10, 100) for _ in range (cols)]
row = len(A)
col = len(A[0])
vec_mult_A = [ 0 for _ in range(rows)]
if cols_A == len(vector):
    print("vector multiplecation of A is: ")
    for i in range (rows):
        for j in range (cols):
            vec_mult_A[i] += A[i][j] * vector[j]
else:
    print("Vector multiplecation is not possible.")

print(vec_mult_A)
