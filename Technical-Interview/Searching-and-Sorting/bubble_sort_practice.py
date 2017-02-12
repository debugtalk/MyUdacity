
def bubble_sort(array, iteration_times):
    iteration_num = 0
    unsorted_length = len(array)
    while unsorted_length > 0:
        for index in range(unsorted_length - 1):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]

            index += 1

        unsorted_length -= 1
        iteration_num += 1

        if iteration_num == iteration_times:
            return array

array = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
assert bubble_sort(array, 1) == [4, 1, 3, 9, 20, 21, 6, 21, 14, 25]

array = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
assert bubble_sort(array, 2) == [1, 3, 4, 9, 20, 6, 21, 14, 21, 25]

array = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
assert bubble_sort(array, 3) == [1, 3, 4, 9, 6, 20, 14, 21, 21, 25]
