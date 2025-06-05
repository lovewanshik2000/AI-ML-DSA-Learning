''' print X,N times'''
def printFunc(x,n):
    if n==0:
        return
    print(x)
    return printFunc(x,n-1)
printFunc(15,5)

'''RECURSION TREE'''
'''
printFunc(15, 5)
│
├── print(15)
└── printFunc(15, 4)
    │
    ├── print(15)
    └── printFunc(15, 3)
        │
        ├── print(15)
        └── printFunc(15, 2)
            │
            ├── print(15)
            └── printFunc(15, 1)
                │
                ├── print(15)
                └── printFunc(15, 0)  # base case: stops recursion'''

'''⏱ Time Complexity (TC):
Each recursive call performs one print(x) operation.
The function calls itself n times until n == 0.
So,Time Complexity = O(n+1)~O(n)
🧠 Space Complexity (SC):
Each recursive call is added to the call stack.
The recursion depth is n, so the maximum number of stack frames is n.
So,Space Complexity = O(n+1)~O(n) (due to recursion stack)'''