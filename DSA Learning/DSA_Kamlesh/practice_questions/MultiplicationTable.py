def multiplicationTable(n):
    res = []
    for i in range(1,11):
        res.append(i*n)
    return res

# Driver code:
n = int(input("Enter number: "))
print(multiplicationTable(n))
