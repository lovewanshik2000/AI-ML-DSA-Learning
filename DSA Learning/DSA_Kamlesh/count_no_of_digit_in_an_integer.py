"""
Write a program to count the number of digits in an integer :-
Example-
Input: 8473
Output: 4
"""

# Solution: - 
n = 8473
num = n
count_digit = 0
while num > 0:
  count_digit += 1
  last_digit = num//10

print("Output :", count_digit)

"""
Time complexity : O(log10(N))
Space Complexity: O(1)
"""


