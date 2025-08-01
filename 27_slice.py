import numpy as np

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

#sice the array to get tthe elements from index 2 to 5
print("Sliced array from index 2 to 5:", arr1[2:6])  # Output: [3 4 5 6]

#slice the array to get the first 3 elements
print("First 3 elements of the array:", arr1[:3])  # Output: [1 2 3]

#slice the array to get the elements from index 5 to the end
print("Elements from index 5 to the end:", arr1[5:])  # Output: [6 7 8 9 10]

#slice the array to get the every other element
print("Every other element of the array:",arr1[::2] ) # Output: [1 3 5 7 9]

arry2 = np.array([[1, 2, 3],
                   [4, 5, 6],
                     [7, 8, 9]])

#Access the element with the value 5.
print("Element with value 5:", arry2[1, 1])  # Output: 5

#slice the arry to get the first two rows and first two columns
print("First two rows and first two columns:\n", arry2[:2, :2])  # Output: [[1 2] [4 5]]

#slice the arry to get the second column
print("Second column of the array:\n", arry2[:, 1])  # Output: [2 5 8]

#slice the array to get the last two rows
print("Last two rows of the array:\n", arry2[-2:, :])# or arry2[1:,:]  # Output: [[4 5 6] [7 8 9]]

#slice the arry to get the first two rows and last two columns
print("First two rows and last two columns:\n", arry2[:2, -2:])  # Output: [[2 3] [5 6]]

#slice the array to get the first two rows and the first two columns
print("First two rows and first two columns:\n", arry2[:2, :2])  # Output: [[1 2] [4 5]]