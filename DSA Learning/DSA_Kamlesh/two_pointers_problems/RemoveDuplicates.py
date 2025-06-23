"""
2️⃣ Remove Duplicates from Sorted Array
Problem:
Remove duplicates in-place from a sorted array nums and return new length.

Example:
nums = [0,0,1,1,2] → Output: 3 (nums = [0,1,2,...])
"""
# ***************************** Brute Force Solution ***************************************
def removeDuplicateBruteForce(arr):
    unique_list = []
    for i in arr:
        if i not in unique_list:
            unique_list.append(i)
    return len(unique_list)

nums = [0,0,1,1,2]
print(removeDuplicateBruteForce(nums))

# Time Complexity: O(n²)
# Space Complexity: O(n)

# ***************************** Using Two Pointers Solution ***************************************
def removeDuplicateTwoPointers(arr):
    if not arr:
        return 0
    left = 0
    for right in range(1, len(arr)):
        if arr[left] != arr[right]:
            left += 1
            arr[left] = arr[right]
    return left + 1

nums = [0,0,1,1,2]
print(removeDuplicateTwoPointers(nums))


# Time Complexity: O(n)
# Space Complexity: O(1)