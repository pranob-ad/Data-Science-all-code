import numpy as np

#list convert to the numpy array
list1 = [1, 2, 3, 4, 5]
array1 = np.array(list1)
print("List:", list1)
print("Numpy Array:", array1)

#numpy array to list
array2 = np.array([6, 7, 8, 9, 10])
list2 = array2.tolist()
print("Numpy Array:", array2)
print("List:", list2)

#numpy array to string
array3 = np.array([11, 12, 13, 14, 15])
string_array = array3.astype(str)
print("Numpy Array:", array3)
print("String Array:", string_array)

#intiger list convert to float numpy array
int_list = [16, 17, 18, 19, 20]
float_array = np.array(int_list, dtype=float)
float_array_alt = float_array.tolist()
print("Integer List:", int_list)
print("Float Numpy Array:", float_array)
print("Float Numpy Array (from list):", float_array_alt)

#float numpy array to integer list
float_array2 = np.array([21.5, 22.5, 23.5, 24.5, 25.5])
int_list2 = float_array2.astype(int).tolist()
print("Float Numpy Array:", float_array2)
print("Integer List:", int_list2)

#numpy array to boolean array
bool_array = np.array([True, False, True, False, True])
print("Boolean Numpy Array:", bool_array)

#boolean array to numpy array
bool_array2 = np.array([1, 0, 1, 0, 1], dtype=bool)
print("Boolean Numpy Array:", bool_array2)

#numpy array to complex number array
complex_array = np.array([1+2j, 3+4j, 5+6j])
print("Complex Numpy Array:", complex_array)