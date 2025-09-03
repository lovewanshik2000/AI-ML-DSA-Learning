"""
Given three integers a, r, and n, where a is the first term of a geometric progression (GP), r is the common ratio, and n is the position of the term you need to find. Your task is to calculate the n-th term of the GP.
Since the result can be very large, return the answer modulo 1000000007 (i.e. 109+ 7).

Examples:

Input: a = 2, r = 2, n = 4
Output: 16
Explanation: The GP series is 2, 4, 8, 16, 32,... in which 16 is the 4th term.
"""
class Solution:
    def mod_pow(self, base, exponent, mod):
        result = 1
        base = base % mod
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % mod
            base = (base * base) % mod
            exponent //= 2
        return result

    def nthTerm(self, a, r, n):
        MOD = 10**9 + 7
        power = self.mod_pow(r, n - 1, MOD)
        return (a * power) % MOD
    
sol = Solution()
print(sol.nthTerm(2, 2, 4))  # Output: 16
