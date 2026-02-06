



def merge(left, right):
    i = j = 0
    results = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            results.append(left[i])
            i += 1
        else:
            results.append(right[j])
            j += 1
    results.extend(left[i:])
    results.extend(right[j:])
    return results

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_hand = arr[mid:]
    right_hand = arr[:mid]
    left_sorted = mergeSort(left_hand)
    right_sorted = mergeSort(right_hand)
    return merge(left_sorted, right_sorted)



print(mergeSort([1,4,3,2,5,8,6]))
print(mergeSort([5,4,3,2,1]))