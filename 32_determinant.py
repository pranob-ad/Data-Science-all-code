#numpy has a sub class called linalg which is used for linear algebra operations
import numpy as np

#meta = np.array([[1, 2, 4], [4, 5, 6], [7, 8, 9]])
meta = np.random.randint(1, 21, (3,3))
print("Random 3x3 martix:\n", meta)

det_meta = np.linalg.det(meta)  # Calculate the determinant of the matrix
print("Determinant of the matrix:\n", det_meta)
if det_meta == 0:
    print("The matrix is singular and does not have an inverse.")
else:
    inv_meta = np.linalg.inv(meta)  # Calculate the inverse of the matrix
    print("Inverse of the matrix:\n", inv_meta)
dot_meta = np.dot(meta, inv_meta)  # Calculate the dot product of the matrix and its inverse
print("Dot product of the matrix and its inverse:\n", dot_meta)

eig_meta = np.linalg.eig(meta)  # Calculate the eigenvalues and eigenvectors of the matrix
print("Eigenvalues and eigenvectors of the matrix:\n", eig_meta)

# Solve a system of linear equations Ax = b
A = np.array([[3, 2], [1, 4]])
b = np.array([5, 6])
x = np.linalg.solve(A, b)  # Solve for x in the equation Ax = b
print("Solution of the system of linear equations Ax = b:\n", x)
# Singular Value Decomposition (SVD)
U, s, Vt = np.linalg.svd(meta)  # Perform Singular Value Decomposition
print("U matrix from SVD:\n", U)
print("Singular values from SVD:\n", s)
print("Vt matrix from SVD:\n", Vt)