print("######################## Brute Force ################################")

def has_pair_brute_force(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i,j]
    return [-1]

arr = [1,2,3,4,6]
target = 6    # Output : [1,3]
print(has_pair_brute_force(arr, target))

arr = [1,2,3,4,6]
target = 0    # Output : [-1]
print(has_pair_brute_force(arr, target))

print()

print("######################## Two Pointers ################################")

def has_pair_two_pointers(arr, target):
    left, right = 0, len(arr)-1
    while left < right:
        curr_sum = arr[left]+arr[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return [-1]



arr = [1,2,3,4,6]
target = 6    # Output : [1,3]
print(has_pair_two_pointers(arr, target))

arr = [1,2,3,4,6]
target = 0    # Output : [-1]
print(has_pair_two_pointers(arr, target))

print()


print("######################## Hash Set ################################")

def has_pair_hashmap(arr, target):
    hashmap = {}
    for i,num in enumerate(arr):
        complement = target-num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
    return [-1]


arr = [1,2,3,4,6]
target = 6    # Output : [1,3]
print(has_pair_hashmap(arr, target))

arr = [1,2,3,4,6]
target = 0    # Output : [-1]
print(has_pair_hashmap(arr, target))

print()

