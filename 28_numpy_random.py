import numpy as np
data1 = np.random.randint(1,20,(3, 4))  # Generate a 3x4 array of random integers between 1 and 20
data = np.random.random((3, 4))  # Generate a 3x4 array of random floats
print("Random integer array of shape (3, 4):\n", data1)
print("Random array of shape (3, 4):\n", data)

"""
for float: random, rand, randn
for int: randint, random_integers, linespace"""

data2 = np.random.randint(-10,20,5)
print(data2)

data2 = np.linspace(1,10,5)
print(data2)

data2 = np.arange(1,10,2)
print(data2)