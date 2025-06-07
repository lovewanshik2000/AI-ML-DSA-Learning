'''sum of 1 to n number '''
def sumNumber(sum,i,n):
    if i>n:
        print(sum)
        return
    sumNumber(sum+i,i+1,n)
sumNumber(0,1,4)
'''🧠 Time and Space Complexity:
Time Complexity (TC): O(n) — it makes one recursive call for each number from i to n.
Space Complexity (SC): O(n) — due to the recursion stack.

🌳 Recursion Tree (for i=1, n=4):

sumNumber(0, 1, 4)
└── sumNumber(1, 2, 4)
    └── sumNumber(3, 3, 4)
        └── sumNumber(6, 4, 4)
            └── sumNumber(10, 5, 4)
                └── print(10)'''
def sumN(n):
    if n==1:
        return 1
    return n+sumN(n-1)
print(sumN(4))

'''🌳 Recursion Tree:
sumN(4)
├─> return 4 + sumN(3)
       ├─> return 3 + sumN(2)
              ├─> return 2 + sumN(1)
                     ├─> return 1  # base case

Step-by-step evaluation:
sumN(1) returns 1
sumN(2) returns 2 + 1 = 3
sumN(3) returns 3 + 3 = 6
sumN(4) returns 4 + 6 = 10 '''

