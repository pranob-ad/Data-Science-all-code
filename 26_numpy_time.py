import numpy as np
import time

size = 1000000

list1 = list(range(size))
list2 = list(range(size))

array1 = np.arange(size)
array2 = np.arange(size)

initial_time = time.time()

product_list = [a * b for a, b in zip(list1, list2)]

#calculate time taken for list comprehension
print("Time taken for list comprehension:", (time.time() - initial_time)*100)
#capture time taken for list comprehension
initial_time = time.time()
product_array = array1 * array2
#calculate execute time
print("Time taken for numpy array multiplication:", (time.time() - initial_time)*100,"seconds")