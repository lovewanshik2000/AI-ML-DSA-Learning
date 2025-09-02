def checkStatus(a, b, flag):
        # code here
        if ((a>=0) != (b>=0)) and flag==False:
            return True
        else:
            False


# Driver Code:
a = 1
b = -1
flag = False

result = checkStatus(a,b,flag)
print(result)

