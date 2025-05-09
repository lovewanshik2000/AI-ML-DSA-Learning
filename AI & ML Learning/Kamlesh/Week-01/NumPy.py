# Learn NumPy
import numpy as np

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

# Create NumPy N-D Array using ndmin function
arr5 = np.array([1,2,3,4,5], ndmin=5)
print("N-D Array:-")
print(arr5, type(arr5))
print(arr5.ndim,"D") 
print()