#!/usr/bin/env python3
def quicksort(array):
    if len(array) < 2:
        return array # base case: arrays with 0 or 1 elements are already "sorted"
    else:
        pivot = array[0] # recursive case
#        less = [i for i in array[1:] if i <= pivot] # subarray of elements less than pivot
#        greater = [i for i in array[1:] if i > pivot] # subarray of elements greater than pivot

        return quicksort(less) + [pivot] + quicksort(greater)

print quicksort([10, 5, 2, 3, 99, 4, 3, 198, 35, 75, 1 , 0.1])
