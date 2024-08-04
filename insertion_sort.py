def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        prev = i - 1
        while prev >= 0 and arr[prev] > current:
            arr[prev + 1] = arr[prev]
            prev -= 1
        arr[prev + 1] = current


insertion_sort([2, 9, 11, 7, 1])
