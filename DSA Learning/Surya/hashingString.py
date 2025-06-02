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