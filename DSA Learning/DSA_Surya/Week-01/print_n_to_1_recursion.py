 # Tail Recursion (N to 1)

def print_n_to_1_tail(n):
    if n == 0:
        return
    print(n)
    print_n_to_1_tail(n - 1)

print_n_to_1_tail(5)  # Output: 5 4 3 2 1

''' Recursion tree
print_n_to_1_tail(5)
├── print(5)
└── print_n_to_1_tail(4)
    ├── print(4)
    └── print_n_to_1_tail(3)
        ├── print(3)
        └── print_n_to_1_tail(2)
            ├── print(2)
            └── print_n_to_1_tail(1)
                ├── print(1)
                └── print_n_to_1_tail(0)  # base case'''

# 🔁 Head Recursion (N to 1)

def print_n_to_1_head(i, n):
    if i > n:
        return
    print_n_to_1_head(i + 1, n)
    print(i)

print_n_to_1_head(1, 5)  # Output: 5 4 3 2 1

'''Recursio  tree 
print_n_to_1_head(1, 5)
└── print_n_to_1_head(2, 5)
    └── print_n_to_1_head(3, 5)
        └── print_n_to_1_head(4, 5)
            └── print_n_to_1_head(5, 5)
                └── print_n_to_1_head(6, 5)  # base case
                    ↑ Backtracking starts
                print(5)
            print(4)
        print(3)
    print(2)
print(1)
'''