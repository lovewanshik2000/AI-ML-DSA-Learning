def longestCommanPrefix(strgs):
    prefix = ''
    for s in strgs:
        if (len(s) < len(prefix) or prefix==''):
            prefix = s
    need = len(strgs)
    count = 0
    result = ''
    while (need != count):
        count = 0 
        for i in strgs:
            if (prefix==i[:len(prefix)]):
                count += 1
        result = prefix
        prefix = prefix[:-1]
    
    if need == count:
        return result
    else:
        return ""

l = ["Flower", "kiow", "Flight"]
print(longestCommanPrefix(l))