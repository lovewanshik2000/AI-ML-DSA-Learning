'''The Fibonacci sequence is:
0, 1, 1, 2, 3, 5, 8, 13, ...
Each number is the sum of the previous two:
F(n)=F(n−1)+F(n−2)
With base cases:
F(0) = 0
F(1) = 1
'''
def fib_recursive(n):
    if n == 0 or n == 1:
        return n
    return (fib_recursive(n-1)+fib_recursive(n-2))
print(fib_recursive(5))  

'''Recursion tree 
fib(5)
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2)
│   │   │   ├── fib(1) → 1
│   │   │   └── fib(0) → 0
│   │   └── fib(1) → 1
│   └── fib(2)
│       ├── fib(1) → 1
│       └── fib(0) → 0
└── fib(3)
    ├── fib(2)
    │   ├── fib(1) → 1
    │   └── fib(0) → 0
    └── fib(1) → 1 '''
