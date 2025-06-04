s="azyxyyzaaaa"
q=["d","a","y","x"]

'''constraints:-'a'<= s[i]<='z' '''
'''ascii of a=97 to z=122'''
# METHOD 1:-
hash_list=[0]*26
for ch in s:
    ascii_val=ord(ch)
    index=ascii_val-97
    hash_list[index]+=1
for ch in q:
    ascii_val=ord(ch)
    index=ascii_val-97
    print(hash_list[index])

'''TIME COMPLEXITY :- O(N+M)
    SPACE COMPLEXITY :- O(1)'''

# METHOD 2:-
hash_list={}
for ch in s:
    hash_list[ch]=hash_list.get(ch,0)+1
for h in q:
    print(hash_list.get(h,0))

''' for ch in s: O(n), where n = len(s)
    for h in q: O(m), where m = len(q)
Inside both loops: dict.get() and assignment are O(1) on average
Total Time Complexity = O(n + m)

In the worst case, all characters in s are unique
⇒ up to O(k) space, where k = number of unique characters in s
Total Space Complexity = O(k)'''
