"""
📌 **************** Problem Statement: Find All Subsequences of a List **********************

Given:
A list seq of distinct integers (or elements), write a function to generate and return all possible subsequences (subsets) of the given list.

Definition:
A subsequence is a sequence that can be derived from the list by deleting zero or more elements without changing the order of the remaining elements.

Example:
If seq = [1, 2, 3]
Then the possible subsequences are:
[[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

"""

"""
📌 Why is this problem important?

    It’s a classic recursion and backtracking problem.

    Forms the basis for many complex problems in combinations, subsets, and dynamic programming.

    Useful in algorithms for decision-making, string processing, and optimization problems.

📌 Explanation of the Approach (Recursive)

We can solve this problem using recursion by breaking it down:

    For each element in the list, we have two choices:

        Include the current element in the subsequence.

        Exclude the current element from the subsequence.

This decision tree grows recursively until the original list is empty.
"""
# *************** Solution:- ******************

def subsequence(seq):
    if not seq:
        return [[]]
    rest = subsequence(seq[1:])
    return rest + [[seq[0]] + sub for sub in rest]

val = subsequence([0,1,2,3])
print(val)
