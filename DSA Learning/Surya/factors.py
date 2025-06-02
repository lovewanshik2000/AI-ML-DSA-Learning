''' FACTORS OF A NUMBER '''
'''METHOD:1'''
def factor(n):
    result = []
    for i in range(1,n+1):
        if n % i==0:
            result.append(i)
    return(result)
print(factor(20))

'''The loop runs from 1 to n, so it iterates n times.
    Inside the loop, n % i is a constant-time operation.
Time Complexity = O(n)
Space Complexity = O(k) (where k is the number of factors)'''

'''METHOD:2'''
def factor1(num):
    result=[]
    for i in range(1,(num//2)+1):
        if num %i==0:
            result.append(i)
    result.append(num)
    return (result)
print(factor1(30))

'''Time Complexity = O(n/2)~ o(n)
Space Complexity = O(k) (where k is the number of factors)'''

''' METHOD:3'''
from math import sqrt
def factor3(num):
    result=[]
    for i in range (1,int(sqrt(num))+1):
        if num%i==0:
            result.append(i)
            if num//i!=i:
                result.append(num//i)
    return (result)
print(factor(36))

'''Time Complexity =  O(√n)'''