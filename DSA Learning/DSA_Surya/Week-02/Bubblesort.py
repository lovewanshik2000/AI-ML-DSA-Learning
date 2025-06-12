'''The bubble sort algorithm works by repeatedly comparing adjacent elements in the array & swapping 
them if they are in the wrong order.Ensuring that after each pass, the largest unsorted element is 
“bubbled” to its correct position.'''

def Bubblesort(arr):
    n=len(arr)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
def Bubblesortdesc(arr):
    n=len(arr)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
p=[12,3,7,5,6]
print(Bubblesort(p)) # [3, 5, 6, 7, 12]
print(Bubblesortdesc(p)) # [12, 7, 6, 5, 3]

'''tc:-0(N(N+1)/2)~O(N**2)
    SC:-O(1) number of variable not change '''