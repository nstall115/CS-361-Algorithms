# modified merge sort from question 2
def mergeSort(arr):
    # 1 element therefore already sorted
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2

    sortL, lInv = mergeSort(arr[:mid])
    sortR, rInv = mergeSort(arr[mid:])
    
    mergeLists, splitInv = merge(sortL, sortR)

    return mergeLists, lInv + rInv + splitInv

def merge(left, right):
    mergeLists = []
    # intialize i and j
    # i = l, r = j, this is to better understand the merge
    l = r = inversions = 0

    # l = i, r = j
    # compare left and right side
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            mergeLists.append(left[l])
            l += 1
        else:
            # left elements create an inversion with the right
            mergeLists.append(right[r])
            r += 1
            inversions += len(left) - l

    mergeLists.extend( left[l:]) # add any leftovers from left
    mergeLists.extend(right[r:]) # add any leftovers from right

    return mergeLists, inversions

ex0 = [1, 2, 3, 4]
ex1 = [4, 3, 2, 1]
ex2 = [2, 4, 1, 3]

for ex in [ex0, ex1, ex2]:
    _, count = mergeSort(ex)
    print(f"{ex} has {count} inversions")