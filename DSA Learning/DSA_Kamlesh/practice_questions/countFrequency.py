"""
input: "aaaabbbcdd"
result="4a3bc2d"
"""

def countFrequency(s):
    result = []
    n = len(s)
    count = 1
    if n==0:
        return ""
    
    for i in range(1, n):
        if s[i]==s[i-1]:
            count +=1
        else:
            result.append(f"{count}{s[i-1]}" if count>1 else s[i-1])
            count = 1
    result.append(f"{count}{s[-1]}" if count>1 else s[-1])
    return ''.join(result)
    
s = "aaaabbbcddeee"
res = countFrequency(s)
print("Output: ", res)
        