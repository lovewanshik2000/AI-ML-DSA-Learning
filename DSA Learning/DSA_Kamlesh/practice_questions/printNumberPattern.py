"""
You are given a number n. You need to generate and print a pattern based on the given value of n.

1. For each row, starting from the first, print numbers in descending order from n down to 1.
2. Each number in a row is repeated as many times as the current row index (starting from n).
3. Instead of printing each row on a new line, separate rows with -1.
4. Instead of a newline at the end of each row, print -1 to indicate row separation. After printing the entire pattern, end the output with -1.

Example:
Input: 3
Output: [3, 3, 3, 2, 2, 2, 1, 1, 1, -1, 3, 3, 2, 2, 1, 1, -1, 3, 2, 1, -1]
"""

def printPat(n):
        #write code here
        l = []
        for i in range(n,0,-1):
            for j in range(n,0,-1):
                l.extend([j]*i)
            l.append("-1")
        print(l)

# Driver Code.
n = int(input("Enter number: "))  
printPat(n)