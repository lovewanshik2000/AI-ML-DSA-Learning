''' REVERSE DIGIT / CHECK PALINDROME '''

def Is_Palindrome (n):
    num = n
    result = 0
    while num > 0 :
        last_digit = num % 10
        result = (result * 10)+last_digit
        num = num // 10
    return (n==result)

print(Is_Palindrome(12314))

'''time complexity==>> O(log₁₀(n))'''