num = [5,7,3,2,6,1,5,9]

def reverse(arr, l, r):
    if l >= r:
        return
    arr[l], arr[r] = arr[r], arr[l]
    reverse(arr, l + 1, r - 1)

reverse(num, 1, 5) # [7,3,2,6,1]
print(num) # [5, 1, 6, 2, 3, 7, 5, 9]
'''TC=O(N/2)~O(N)
    SC=O(N/2)~O(N)'''

########### USING WHILE LOOP #########
n=len(num)
left=0
right=n-1
while left<right:
     # Swap elements at left and right
    num[left], num[right] = num[right], num[left]
    
    # Move pointers
    left += 1
    right -= 1

print(num)  # This will print the reversed entire list
'''TC=O(N/2)~O(N)
    SC=O(N/2)~O(N)'''