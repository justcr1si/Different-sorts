def quicksort(array):
    """Быстрая сортировка."""
    len_array = len(array)

    if len_array <= 1:
        return array

    middle_element_index = len_array // 2
    pivot = array[middle_element_index]
    left, center, right = partition(array, pivot)
    return quicksort(left) + center + quicksort(right)


def partition(array, pivot):
    """
    Разбивает массив на три разных массива относительно опорного элемента.
    """
    left, center, right = [], [], []
    for item in array:
        if item < pivot:
            left.append(item)
        elif item > pivot:
            right.append(item)
        else:
            center.append(item)
    # print(left, center, right)
    return left, center, right


arr = list(map(int, input().split()))
result = quicksort(arr)
print(result)
