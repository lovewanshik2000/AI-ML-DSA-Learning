from typing import List
import time

# ✅ Brute-Force Solution (O(n²) Time)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    
# Driver Code
# ✅ Driver Code
sol = Solution()

print("Brute-Force Results:")
start_time = time.time()
print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
end_time = time.time()
print("Brute-Force Execution Time: {:.10f} seconds".format(end_time - start_time))

print(sol.twoSum([3, 2, 4], 6))       # Output: [1, 2]
print(sol.twoSum([3, 3], 6))  


# ✅ Optimized Solution (O(n) Time)
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in num_idx:
                return [num_idx[diff], i]
            num_idx[n] = i

# ✅ Driver Code
sol = Solution()

print("\nOptimized Results:")
start_time = time.time()
print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
end_time = time.time()
print("Brute-Force Execution Time: {:.10f} seconds".format(end_time - start_time))

print(sol.twoSum([3, 2, 4], 6))       # Output: [1, 2]
print(sol.twoSum([3, 3], 6))  



# ******************************* Test the time Complexity on large dataset *********************************************
# from typing import List
# import time

# # ✅ Brute-Force Solution (O(n²) Time)
# class SolutionBrute:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

# # ✅ Optimized Solution (O(n) Time)
# class SolutionOptimized:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         num_idx = {}
#         for i, n in enumerate(nums):
#             diff = target - n
#             if diff in num_idx:
#                 return [num_idx[diff], i]
#             num_idx[n] = i

# # ✅ Test Data (Large List)
# nums = list(range(1, 10001))  # 1 to 10000
# target = 19999  # Last two numbers: 9999 + 10000

# # ✅ Brute-Force Execution Time
# sol_brute = SolutionBrute()
# start_time = time.time()
# result_brute = sol_brute.twoSum(nums, target)
# end_time = time.time()
# print("Brute-Force Result:", result_brute)
# print("Brute-Force Execution Time: {:.6f} seconds".format(end_time - start_time))

# # ✅ Optimized Execution Time
# sol_optimized = SolutionOptimized()
# start_time = time.time()
# result_optimized = sol_optimized.twoSum(nums, target)
# end_time = time.time()
# print("Optimized Result:", result_optimized)
# print("Optimized Execution Time: {:.6f} seconds".format(end_time - start_time))
