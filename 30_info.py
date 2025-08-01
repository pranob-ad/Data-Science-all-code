import numpy as np

a = np.array([1,2,3,4])
b = np.array([4])
print(a+b)
print(a-b)
print(a*b)
print(a/b)


# Create an array:
# arr = [[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]]
# a) Add the scalar value 10 to each element of arr (use broadcasting).
# b) Add the array [10, 20, 30] to arr (use broadcasting).

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print(arr+10)
print(arr+np.array([10,20,30]))


""" Universal Functions in numpy
np.sin(), np.cos(), np.tan(), np.sqrt(), np.exp(), np.log()
"""

val = np.array([0, np.pi, np.pi/2, np.pi/4])
print(a)
print(np.sin(val))
print(np.cos(val))
print(np.tan(val))
