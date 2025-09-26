"""
A. Fixed-Size Window:
   The window size k is given.

Pattern:

1. Expand the window by adding the next element.

2. When window size > k, shrink from the left.

3. Track the required metric (sum, max, etc.).

Example: Maximum sum of a subarray of size k.
"""

def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]   # add next, remove first
        max_sum = max(max_sum, window_sum)
    return max_sum



# Drive code
arr = [1,2,3,4,5]
k = 3
print("Max Sum of Subarray: ", max_sum_subarray(arr,k))