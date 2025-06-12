''' factorial of a number '''
'''n!=n*(n-1)*(n-2)*......*2*1'''
def factorial(n):
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)
print(factorial(4)) 