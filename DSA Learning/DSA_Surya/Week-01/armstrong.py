''' ARMSTRONG NUMBER '''
def armstrong_number(n):
    num = n 
    tod= len(str(n))
    total = 0
    while num > 0 :
        last_digit = num % 10
        total= total+(last_digit**tod)
        num = num // 10
    return (total == n)

print(armstrong_number(153))

'''Time Complexity -->>	O(log₁₀(n))
Space Complexity -->>	O(1)'''