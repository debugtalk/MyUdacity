
def merge_sort(array):
    if len(array) <= 1:
        return array

    left = merge_sort(array[:len(array)//2])
    right = merge_sort(array[len(array)//2:])

    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))

    if len(left) > 0:
        result.extend(merge_sort(left))
    else:
        result.extend(merge_sort(right))
    return result


array = [21, 4, 1, 3, 9, 20, 25]
print(merge_sort(array))
