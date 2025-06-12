''' Recursion Theory :- Recursion is a programming technique where a function calls itself in order to solve a problem.'''
def countdown(n):
    if n == 0:  # Base case: When n == 0, it stops
        print("Done!")
    else:
        print(n)
        countdown(n - 1)

countdown(3)
'''Recursion Tree for countdown(3)
countdown(3)
  └── prints: 3
  └── countdown(2)
        └── prints: 2
        └── countdown(1)
              └── prints: 1
              └── countdown(0)
                    └── prints: Done!   (hits the base case, prints Done!, and returns)'''
################################
''' Stack Overflow Error :- A stack overflow error happens when a function calls itself too many times without stopping, 
    using up all the memory reserved for tracking those calls (the call stack).
    This usually occurs with infinite or very deep recursion.'''

# def infinite():
#     print("hi")
#     infinite()

# infinite()  #RecursionError: maximum recursion depth exceeded

##########################################

'''example of recursion'''
count = 5  # Initialize count to control recursion depth

def func():
    global count
    if count == 0:
        return
    print("hi")
    count -= 1  # Decrease count to move towards base case
    func()

func()
#################################
'''Head Recursion :-
The recursive call is the first operation (before doing anything else).
The function processes after recursion returns.'''
def head_recursion(n):
    if n == 0:
        return
    head_recursion(n - 1)  # Recursive call first
    print(n)               # Process AFTER the recursive call
head_recursion(3)

'''
head_recursion(3)
 └─ head_recursion(2)
      └─ head_recursion(1)
           └─ head_recursion(0) → return
           └─ prints: 1
      └─ prints: 2
 └─ prints: 3''''

#######################################

'''Tail Recursion
The recursive call is the last statement in the function.
Nothing happens after the function calls itself.'''
def tail_recursion(n):
    if n == 0:
        return
    print(n)         # Do something
    tail_recursion(n - 1)  # Recursive call is the LAST thing
tail_recursion(3)
''' Recursion tree
tail_recursion(3)
 └─ prints: 3
 └─ tail_recursion(2)
      └─ prints: 2
      └─ tail_recursion(1)
           └─ prints: 1
           └─ tail_recursion(0) → return'''

'''🧠 Tip:
Tail recursion = "Do, then call"
Head recursion = "Call, then do"'''
'''Time Complexity for Both = O(n+1)~O(n)
    Space Complexity for both =  O(n+1)~O(n)
'''