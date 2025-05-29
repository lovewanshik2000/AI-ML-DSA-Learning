'''
NumPy is used to work with arrays.
It provides fast operations on arrays and matrices.
It is essential for scientific computing in Python.
To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, 
and it will be converted into an ndarray

**indexing**
Array indexing is the same as accessing an array element.

**Slicing arrays**
Slicing in python means taking elements from one given index to another given index.

We pass slice instead of index like this: [start:end].
We can also define the step, like this: [start:end:step].

arr[row_start:row_end, col_start:col_end] → slicing a submatrix.
arr[row_index, col_index] → single value.
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
print("slicing",arr[1:4:2])

# 📌 Another 1-D array (using tuple)
arr1 = np.array((1, 2, 3, 4, 5, 8))
print("1D array (from tuple):", arr1)
print("Type:", type(arr1))
print("Dimensions:", arr1.ndim)
print("Sum of elements at index 2 and 3:", arr[2], "+", arr[3], "=", arr[2] + arr[3]) # Output: 7
print("-" * 50)

# 📌 Create a 0-D array
arr = np.array(42)
print("0D array:", arr)
print("Dimensions:", arr.ndim)
print("-" * 50)

# 📌 Create a 2-D array
arr = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])
print("2D array:\n", arr)
print("Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("-" * 50)

# 🧾 Access specific elements in the 2D array
print("Element at 1st row, 2nd column (arr[0, 1]):", arr[0, 1])   # Output: 2
print("Element at 2nd row, 5th column (arr[1, 4]):", arr[1, 4])   # Output: 10
print("Last element from 2nd row (arr[1, -1]):", arr[1, -1])    # Output: 10
print("-" * 50)

# 1️⃣ Slice rows 0 to 1 (exclusive of 2), and columns 1 to 3 (exclusive of 4)
print("arr[0:2, 1:4] → Rows 0 to 1, Columns 1 to 3:\n", arr[0:2, 1:4])
# Output:
# [[2 3 4]
#  [7 8 9]]
print("-" * 50)

# 2️⃣ Slice rows 0 to 1 (0:2), and pick column 2
print("arr[0:2, 2] → Rows 0 to 1, only column 2:\n", arr[0:2, 2])
# Output:
# [3 8]
print("-" * 50)

# 3️⃣ From row 1, slice columns 1 to 3 (1:4)
print("arr[1, 1:4] → Row 1, columns 1 to 3:\n", arr[1, 1:4])
# Output:
# [7 8 9]
print("-" * 50)

# 1️⃣ Slice a part of the array (this is a VIEW)
view_arr = arr[0:2, 1:4]
print("View (arr[0:2, 1:4]):\n", view_arr)

# Modify the view
view_arr[0, 0] = 999
print("Modified View:\n", view_arr)
print("Array After View Modification:\n", arr)  # arr is also modified!
print("-" * 50)

# 2️⃣ Create a COPY of a slice
copy_arr = arr[0:2, 2:5].copy()
print("Copy (arr[0:2, 2:5].copy()):\n", copy_arr)

# Modify the copy
copy_arr[0, 0] = 888
print("Modified Copy:\n", copy_arr)
print("Array After Copy Modification (original remains unchanged):\n", arr)

# 📌 Create a 3-D array
arr = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])
print("3D array:\n", arr)
print("Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("-" * 50)

# 🧾 Access a specific element in the 3D array
print("Element at arr[0, 1, 2]:", arr[0, 1, 2])   # Output: 6

# 📌 Create a 5-D array using ndmin
arr = np.array([1, 2, 3, 4], ndmin=5)
print("5D array:\n", arr)
print("Dimensions:", arr.ndim)
print("-" * 50)

