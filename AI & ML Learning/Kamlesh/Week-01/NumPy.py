# Learn NumPy
import numpy as np

# ******************************** Create Array ************************************************
# 0-D Arrays
zero_arr = np.array(45)
print("0-D Array:-")
print(zero_arr, type(zero_arr))
print(zero_arr.ndim,"D") 
print()

# Create NumPy 1-D Array using List
li = [1,2,3,4]
arr = np.array(li)
print("1-D Array using List:-")
print(arr, type(arr))
print(arr.ndim,"D") 
print()

# Create NumPy 1-D Array using Tuple
arr1 = np.array((1, 2, 3, 4, 5))
print("1-D Array using Tuple:-")
print(arr1, type(arr1))
print(arr1.ndim,"D") 
print()

# Create NumPy 2-D Array using nested list
arr2 = np.array([[1,2,3,4],[4,5,6,7]])
print("2-D Array:-")
print(arr2)
print(arr2, type(arr2))
print(arr2.ndim,"D") 
print()

# Create NumPy 3-D Array using nested list
arr3 = np.array([[[1, 2, 3], [4, 5, 6], [1, 2, 3], [4, 5, 6]]])
print("3-D Array:-")
print(arr3, type(arr3))
print(arr3.ndim,"D") 
print()

# Create NumPy N-D Array using ndmin function with nth parameter
arr5 = np.array([1,2,3,4,5], ndmin=5)
print("N-D Array:-")
print(arr5, type(arr5))
print(arr5.ndim,"D") 
print()


# ******************************** Array Indexing ************************************************
import numpy as np

"""
Access Array Elements

Array indexing is the same as accessing an array element.

You can access an array element by referring to its index number.

The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.
"""


#  One-D Array
# Get the first element from the following array:
arr = np.array([1, 2, 3, 4])
print("First Element",arr[0]) 
# print(arr[0:2]) 

# Get the second element from the following array.
arr = np.array([1,2,3,4])
print("Second Element",arr[1])

# Get third and fourth elements from the following array and add them.
arr = np.array([1,2,3,4])
print("Sum of third and fourth Element",arr[2] + arr[3])


# ########################################## 2-D array indexing ##################################################

"""
Access 2-D Arrays:

To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.

Think of 2-D arrays like a table with rows and columns, where the dimension represents the row and the index represents the column.

"""

arr = np.array([[1,2,3,4], [4,5,6,7]])
print("2-D Array first element", arr[0,0])
print("2-D Array last element", arr[1,3])
print(arr[0][0], arr[-1][-1])
print(arr[0:2, 2:])

# Access the element on the first row, second column:
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1]) 

# Access the element on the 2nd row, 5th column:
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('5th element on 2nd row: ', arr[1, 4])



# ########################################## 3-D array indexing ##################################################
"""
Access 3-D Arrays

To access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element.
"""

# Access the third element of the second array of the first array:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2]) 

# Negative Indexing
# Use negative indexing to access an array from the end.
# Print the last element from the 2nd dim:

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1]) 