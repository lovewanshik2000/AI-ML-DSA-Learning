'''
NumPy is used to work with arrays.
It provides fast operations on arrays and matrices.
It is essential for scientific computing in Python.
To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, 
and it will be converted into an ndarray
'''
import numpy as np

# 📌 Get the NumPy version
print("NumPy version:", np.__version__)
print("-" * 50)

# 📌 Create a 1-D array
arr = np.array([1, 2, 3, 4, 5])
print("1D array:", arr)
print("Type:", type(arr))
print("Dimensions:", arr.ndim)
print("-" * 50)

# 📌 Another 1-D array (using tuple)
arr1 = np.array((1, 2, 3, 4, 5, 8))
print("1D array (from tuple):", arr1)
print("Type:", type(arr1))
print("Dimensions:", arr1.ndim)
print("-" * 50)

# 📌 Create a 0-D array
arr = np.array(42)
print("0D array:", arr)
print("Dimensions:", arr.ndim)
print("-" * 50)

# 📌 Create a 2-D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:\n", arr)
print("Dimensions:", arr.ndim)
print("-" * 50)

# 📌 Create a 3-D array
arr = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[1, 2, 3], [4, 5, 6]]
])
print("3D array:\n", arr)
print("Dimensions:", arr.ndim)
print("-" * 50)

# 📌 Create a 5-D array using ndmin
arr = np.array([1, 2, 3, 4], ndmin=5)
print("5D array:\n", arr)
print("Dimensions:", arr.ndim)
print("-" * 50)
