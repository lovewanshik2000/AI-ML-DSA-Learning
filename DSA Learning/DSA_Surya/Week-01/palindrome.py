## METHOD : 1

def is_palindrome(name):
    n = len(name)
    left = 0
    right = n - 1
    while left < right:
        if name[left] != name[right]:
            return False
        left += 1
        right -= 1
    return True
print(is_palindrome("nitin"))  # Output: True
print(is_palindrome("hello"))  # Output: False
'''
🔹  Time Complexity (TC): O(n)
You check each pair of characters from start and end.
Only n/2 comparisons are needed ⇒ still linear.
Tc = O(n/2)~ O(n)

🔹 Space Complexity (SC): O(1)
Constant space: just a few pointer variables (left, right)
No stack, no new memory created.'''

## METHOD : 2
def is_palindrome_recursive(name, left, right):
    if left >= right:
        return True
    if name[left] != name[right]:
        return False
    return is_palindrome_recursive(name, left + 1, right - 1)

# Call it like this:
print(is_palindrome_recursive("surya", 0, len("surya") - 1))  # True


'''is_palindrome_recursive("nitin", 0, 4) → 'n' == 'n'
│
├── is_palindrome_recursive("nitin", 1, 3) → 'i' == 'i'
│   │
│   ├── is_palindrome_recursive("nitin", 2, 2) → single char → return True
│   │
│   └── returns True
│
└── returns True'''
'''🔹  Time Complexity (TC): O(n)
You check each pair of characters from start and end.
Only n/2 comparisons are needed ⇒ still linear.
Tc = O(n/2)~ O(n)

🔹 Space Complexity (SC): O(1)
Each recursive call adds a stack frame.
For input of size n, there will be ~n/2 recursive calls.
Thus, space complexity = O(n) due to call stack..'''