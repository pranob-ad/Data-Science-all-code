''' Generate random floating values using randn()
for the range between 20 to 200 of 1D array (size=20)
'''
import numpy as np

scaled_number = 20 + (200-20)*np.random.rand(20)
print(scaled_number)

original = np.random.randn(20)
print(original)

scaled_number = 20 + (200-20)*((original-original.min())/(original.max()-original.min()))
print(scaled_number)