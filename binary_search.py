from inspect import stack

wins = ['Алгоритмист', 'Антон', 'жил', 'на', 'полигоне', 'пятьсот', 'суток']
my_ticket = wins[wins.index('полигоне')]


def print_call_stack():
    print([frame.function for frame in stack()])


def binary_search(arr, x, left, right):
    if right < left:
        return None
    print_call_stack()
    mid = (left + right) // 2
    if arr[mid] == x:
        return mid
    if x < arr[mid]:
        return binary_search(arr, x, left, mid - 1)
    else:
        return binary_search(arr, x, mid + 1, right)


index = binary_search(wins, my_ticket, left=0, right=(len(wins) - 1))
print(index)
