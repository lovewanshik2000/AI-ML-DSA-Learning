def romanToInteger(s):
    translate = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    no = 0
    s = s.upper()

    s = s.replace("IV","IIII")   # 4
    s = s.replace("IX","VIIII")  # 9
    s = s.replace("XL","XXXX")   # 40
    s = s.replace("XC","LXXXX")  # 90
    s = s.replace("CD","CCCC")   # 400
    s = s.replace("CM","DCCCC")  # 900

    for char in s:
        no += translate[char] 
    return no

print(romanToInteger("XIV"))


# Time Complexity: O(N)
# Space Complexity: O(N)
