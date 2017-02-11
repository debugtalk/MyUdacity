"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    length = len(input_array)
    index = length // 2
    found_value = input_array[index]
    while True:
        if value == found_value:
            return index
        if value > found_value:
            index = (index + length) // 2
        else:
            index = index // 2

        found_value = input_array[index]
        if index == length - 1 and value != found_value:
            return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
assert binary_search(test_list, test_val1) == -1
assert binary_search(test_list, test_val2) == 4
assert binary_search(test_list, 1) == 0
assert binary_search(test_list, 29) == 6
