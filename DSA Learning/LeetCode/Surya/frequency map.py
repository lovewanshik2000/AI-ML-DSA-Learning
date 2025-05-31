''' frequency map:- keeps track of how many times each item appears.
    Hashing :-	Fast data access using a unique key '''

''' GIVEN:-
num = [5,6,7,7,1,9,111]'''

# METHOD :1
num = [5,6,7,7,1,9,111,9,4,4,4,2]
freq_map =dict()
for i in range (0,len(num)):
    if num[i]in freq_map :
        freq_map[num[i]]=freq_map[num[i]]+1
    else:
        freq_map[num[i]]=1
print(freq_map)

'''time comlexity:-Loop through list num:
Runs n times → O(n) where n = len(num)
Inside the loop:
num[i] in freq_map: Dictionary lookup → Average case O(1)
freq_map[num[i]] = ...: Dictionary update → Average case O(1)
✅ Both lookup and insert/update in a Python dictionary are O(1) on average due to hashing.'''

# METHOD :2
nums = [3,3,3,4,5,6,4,6,5,7,9]
freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1
print(freq)

'''time complexity:- You are looping through the list nums once
→ This takes O(n) time, where n is the length of the list

freq.get(num, 0) and freq[num] = ... are both dictionary operations
→ Dictionary get and assignment are average O(1) (constant time), thanks to hashing