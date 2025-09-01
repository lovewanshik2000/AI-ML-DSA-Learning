def checkOddEven(x):
    # code here
    if x%2 == 0:
        return "Even"
    else:
        return "Odd"


# Driver Code:
x = int(input("Enter number : "))
result = checkOddEven(x)
print(result)