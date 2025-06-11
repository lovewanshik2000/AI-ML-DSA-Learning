'''✅ Selection Sort Algorithm:
Selection sort works by repeatedly finding the minimum element from the unsorted part and putting it at the beginning.'''

def Selectionsort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
def Selectionsortdesc(arr):
    n=len(arr)
    for i in range(n):
        max_index=i
        for j in range(i+1,n):
            if arr[j]>arr[max_index]:
                max_index=j
        arr[i],arr[max_index]=arr[max_index],arr[i]
    return arr
p=[12,3,7,5,6]
print(Selectionsort(p)) # ascending order
print(Selectionsortdesc(p)) # descending order