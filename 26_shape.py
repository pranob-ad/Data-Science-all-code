#generate a numpy dimention of 1024 x 728
import numpy as np

# Reshape an array
a= np.arange(9)
b = a.reshape(3, 3)
print("Original array:\n", a)
print("Reshaped array:\n", b)

#multidimensional array shape as
a_list = [[[1,2,3], [3,4,5]],[[2,4,5],[6,7,8]]]

print(len(a_list))
print(len(a_list[0]))
print(len(a_list[0][0]))

a_array = np.array(a_list)
print(a_array.shape)

#a_array = np.array([i for i in range(1024 * 728)]for j in range(728))
a_array = np.arange(1024*728) 
array1 = a_array.reshape(1024, 728)
#above to line merge in one line
#a_array = np.array(1024 * 728).reshape(1024 * 728)
print("Shape of the array:", a_array.shape)
print("Shape of the array:", array1.shape)

#nul margin array
zero = np.zeros((3, 3))
print("Shape of the null margin array:")
print(zero)
print(zero[0:2])
print(zero[0:2, 0:2])