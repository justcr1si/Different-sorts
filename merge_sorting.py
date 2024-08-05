def merge_sort(array):
    if len(array) <= 1:
        return array

    left = merge_sort(array[0: len(array) // 2])
    right = merge_sort(array[len(array) // 2: len(array)])

    return merge(left, right)


def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    return result + left[left_index:] + right[right_index:]


test_array = [5, 4, 9, 10, 8, 3, 11, 1, 7, 6, 2]
print(merge_sort(test_array))
