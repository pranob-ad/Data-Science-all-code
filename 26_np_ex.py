import numpy as np
a= [1, 'age', 3.14, True, None]
arr = np.array(a)
print(arr)


np.full((2, 3), 5)  # Create a 2x3 array filled with the value 5
print(np.full((2, 3), 5))

np.identity(3)  # Create a 3x3 identity matrix
print(np.identity(3))
np.eye(3)  # Create a 3x3 identity matrix using eye
print(np.eye(3))

b = np.array([1,2,3,4,5,6])
bool_b = (b > 1) & (b < 4) #b > 2
print(bool_b)
print(b[bool_b])
print(b[b%2==0])