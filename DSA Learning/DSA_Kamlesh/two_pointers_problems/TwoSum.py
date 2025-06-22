"""
📌 Problem:
Given a sorted array and a target sum, find if there exists a pair with the given sum.

Example:
Input: arr = [1, 2, 3, 4, 6], target = 6
Output: True (because 2+4 = 6)

# **************************************** Traditional (Brute Force) Approach *************************************************
✅ Idea: Check all possible pairs using nested loops.

📖 Algorithm:
1. Run two nested loops.

2. For each element arr[i], check every other element arr[j].

3. If arr[i] + arr[j] == target, return True.

4. If no pair found, return False.

📦 Time Complexity: O(n²)
📦 Space Complexity: O(1)
"""

print("######################## Brute Force ################################")

def has_pair_brute_force(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i,j]
    return [-1]

arr = [1,2,3,4,6]
target = 6    # Output : [1,3]
print(has_pair_brute_force(arr, target))

arr = [1,2,3,4,6]
target = 0    # Output : [-1]
print(has_pair_brute_force(arr, target))

print()


# ************************************* Optimized Approach using Two Pointers ********************************************
"""
✅  Idea: Since the array is sorted, we can use two pointers — one starting from the beginning and one from the end.
    If array is not sorted then apply arr.sort() function then apply two pointer.

📖 Algorithm:
1. Initialize two pointers: left = 0 and right = n-1

2. While left < right:
        (I) Calculate curr_sum = arr[left] + arr[right]
        (II) If curr_sum == target, return True.
        (III) If curr_sum < target, move left pointer rightward.
        (IV) If curr_sum > target, move right pointer leftward.

3. If no pair found, return False.

📦 Time Complexity: O(n)
📦 Space Complexity: O(1)
"""
print("######################## Two Pointers ################################")

def has_pair_two_pointers(arr, target):
    left, right = 0, len(arr)-1
    while left < right:
        curr_sum = arr[left]+arr[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return [-1]



arr = [1,2,3,4,6]
target = 6    # Output : [1,3]
print(has_pair_two_pointers(arr, target))

arr = [1,2,3,4,6]
target = 0    # Output : [-1]
print(has_pair_two_pointers(arr, target))

print()

# ************************************ Optimized Algorithm (HashMap-based Two Sum) ******************************************
"""
✅  Idea: Since the array is sorted, we can use two pointers — one starting from the beginning and one from the end.
    If array is not sorted then apply arr.sort() function then apply two pointer.

📖 Algorithm:
1. Use a HashMap (dictionary) to store the numbers you’ve seen with their indices.

2. For each number, 
    (I)Find complement target - num 
    (II) Check if its complement (target - num) exists in the map.
        (A) If found, return the indices.
    (III) If not, add the number with its index to the map.
3. If no pair found, return False.

📦 Time Complexity: O(n)
📦 Space Complexity: O(n)
"""
print("######################## Hash Map ################################")

def has_pair_hashmap(arr, target):
    hashmap = {}   # create a map
    for i,num in enumerate(arr):
        complement = target-num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
    return [-1]


arr = [1,2,3,4,6]
target = 6    # Output : [1,3]
print(has_pair_hashmap(arr, target))

arr = [1,2,3,4,6]
target = 0    # Output : [-1]
print(has_pair_hashmap(arr, target))

print()

