def palindrome_no(x):
    """
    check palindrome number without using string.
    """
    if x<0 or (x%10==0 and x!=0):
        return False
    rev = 0
    while x>rev:
        last_digit = x%10
        rev = rev*10 + last_digit
        x = x//10
    
    if x == rev or (x == rev//10):
        return True
    return False
        
# x = 121     # True
# x = 1221    # True
x = 12331   # False

print(palindrome_no(x))

