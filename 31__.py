'''
create a numpy array with 26 equally spaced values in range 1 to 100
create a numpy array with values in range 50 - 100 with 3 spaced apart
create a 5 x 5 matrix of number 27
create identity martix of 3 x 3
'''
import numpy as np
a = np.linspace(1, 100, 26)  # Create a numpy array with 26 equally spaced values in range 1 to 100
print(a)
b = np.arange(50, 101, 3)  # Create a numpy array with values in range 50 - 100 with 3 spaced apart
print(b)
c = np.full((5, 5), 27)  # Create a 5 x 5 matrix of number 27
print(c)
d = np.identity(3)  # Create identity matrix of 3 x 3
print(d)