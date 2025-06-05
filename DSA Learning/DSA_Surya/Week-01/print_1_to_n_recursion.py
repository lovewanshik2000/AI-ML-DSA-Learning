''' Print numbers from 1 to N using both head and tail recursion.'''
'''✅ Head Recursion'''
def headfunc(i,n):
    if i>n:
        return
    headfunc(i+1,n)
    print(i)
# Reverse logic: print from backtracking
headfunc(1,4) # output 4 3 2 1
''' Recursion tree
print_1_to_n_head(1, 5)
└── print_1_to_n_head(2, 5)
    └── print_1_to_n_head(3, 5)
        └── print_1_to_n_head(4, 5)
            └── print_1_to_n_head(5, 5)
                └── print_1_to_n_head(6, 5)  # Base case: return
                    ↑ Backtracking starts
                print(5)
            print(4)
        print(3)
    print(2)
print(1)
''''

# For actual 1 to N, call in reverse:
def print_1_to_n_head_correct(i, n):
    if i>n:
        return
    print_1_to_n_head_correct(i, n - 1)
    print(n)

print_1_to_n_head_correct(1, 8)  # Output: 1 2 3 4 5 6 7 8
''' Recursion tree 
print_1_to_n_head_correct(1, 5)
└── print_1_to_n_head_correct(1, 4)
    └── print_1_to_n_head_correct(1, 3)
        └── print_1_to_n_head_correct(1, 2)
            └── print_1_to_n_head_correct(1, 1)
                └── print_1_to_n_head_correct(1, 0)  # Base case
                    ↑ Backtracking starts
                print(1)
            print(2)
        print(3)
    print(4)
print(5)
'''

''' ✅ Tail Recursion '''
def number(i,n):
    if i>n:
        return
    print(i)  # the action happens before recursion
    return number(i+1,n)
number(1,5)  # output 1 2 3 4 5

'''recursion tree'''
'''
number(1, 5)
│
├── print(1)
└── number(2, 5)
    │
    ├── print(2)
    └── number(3, 5)
        │
        ├── print(3)
        └── number(4, 5)
            │
            ├── print(4)
            └── number(5, 5)
                │
                ├── print(5)
                └── number(6, 5)  # base case'''

'''TC = O(n)
    SC = O(n)'''