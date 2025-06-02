''' HASHING IN PYTHON :-  storing data in a data structure like a dictionary or set using keys (hashes) 
for very fast storing and retrieving.'''
''' Count how many times each element from list m appears in list n.'''
'''constraints :- 
=> 1<=n[i]<=10
=> n can have 10**8 elements
=> m can have 10**8 elements '''
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,112,1,9,5,67,2]
# METHOD :1
# for num in m:
#     count=0
#     for x in n:
#         if num == x:
#             count= count+1
#     print(f"{num} appears {count} time(s) in n")

''' time complexity :- O(MxN)
What does this mean practically?
If M and N are large (like up to 10⁸), the total operations can be up to:

10**8 x 10**8 = O(10**16)
This is too large to run in any reasonable time on modern computer
(typical time limits for programs are ~1-10 seconds, which is roughly 10⁸ to 10⁹ operations).
 it will give TLE ERROR .
 space complexity :- 0(1)'''

# METHOD :2
''' we have to make optimal solution here we create one list of length is (n+1) because 1<=n[i]<=10'''
# hash_list=[0]*11
# for num in n:
#     hash_list[num]=hash_list[num]+1
# for x in m:
#     if x<1 or x>10:
#         print(0)
#     else:
#         print(hash_list[x])
''' time complexity :- O(M+N)
What does this mean practically?
If M and N are large (like up to 10⁸), the total operations can be up to:

10**8 + 10**8 = O(2x10**8) ~ O(10**8)
 it will NOT give TLE ERROR .
 space complexity :- O(1)'''

# METHOD 3:-
freq_dict=dict()
for num in n :
    freq_dict[num]=freq_dict.get(num,0)+1
for x in m :
    print(f"{x} appears {freq_dict.get(x, 0)} time(s) in n")
    print (freq_dict.get(x, 0))
