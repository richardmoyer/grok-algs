#!/usr/bin/env python3

def binary_search(list, item):
    low = 0 #low and high keep track of which part of the list you'll search in
    high = len(list) -1

    while low <= high: # wont have narrowed it down to one element
        mid = (low + high) # check the middle element
        guess = list[mid]
        if guess == item: # found the item
            return mid
        if guess > item: # guess was to high
            high = mid -1
        else:              # guess to low
            low + mid + 1
            return None # item doesnt exist

my_list = [1, 3, 5, 7, 9]

print binary_search(my_list, 3)
print binary_search(my_list, -1)

print binary_search(my_list, 9)
