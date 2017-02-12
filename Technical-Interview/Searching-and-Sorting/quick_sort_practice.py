"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        # get last item from array as pivot
        pivot = array[-1]
        # move elements<pivot in array-{pivot} to the left side
        small_part = [x for x in array[0:-1] if x < pivot]
        # move elements>=pivot in array-{pivot} to the right side
        big_part = [x for x in array[0:-1] if x >= pivot]
        # recursively quicksort left and right part and combine them together
        return quicksort(small_part) + [pivot] + quicksort(big_part)

def quick_sort(array):
    return \
        array if len(array) <= 1 \
        else quick_sort([x for x in array[1:] if x < array[0]]) \
            + [array[0]] \
            + quick_sort([x for x in array[1:] if x >= array[0]])

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
assert quicksort(test) == [1, 3, 4, 6, 9, 14, 20, 21, 21, 25]
assert quick_sort(test) == [1, 3, 4, 6, 9, 14, 20, 21, 21, 25]
