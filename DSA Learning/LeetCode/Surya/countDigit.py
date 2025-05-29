''' TO COUNT THE DIGIT '''

def CountDigit(n):
    num = n
    count = 0
    while num > 0 :
        count += 1
        num = num // 10
    return count

print(CountDigit(7895))

# ANOTHER METHOD

from math import *

def countdigit (n):
    return(int(log10(n)+1))

print (countdigit(789)) # output : 3
# print (countdigit(0)) # output : ValueError: math domain error
# print (countdigit(-789)) # output : ValueError: math domain error

''' if n = (0 or -ve number) then it give ValueError: math domain error
    Note:-  abs() returns the absolute (positive) value:
            abs(-789) = 789
    abs(n) = converting negative numbers to positive before taking the log'''

# CORRECT WAY
def countdigit(n):
    if n == 0:
        return 1  # log10(0) is undefined
    return int(log10(abs(n)) + 1)

print (countdigit(789)) # output : 3
print (countdigit(0)) # output : 1
print (countdigit(-789)) # output : 3

'''🔁 Comparison:
Method	Time Complexity
int(log10(abs(n)) + 1) ==>> O(1)
Manual digit count using loop ==>> O(log₁₀(n))'''