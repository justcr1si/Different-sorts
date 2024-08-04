def template_sort(data, data_template):
    start_index = 1
    for element in data_template:
        for i in range(start_index, len(data)):
            current = data[i]
            previous = i - 1
            if current == element:
                while previous >= start_index - 1:
                    if previous == start_index - 1:
                        data[previous + 1] = current
                    else:
                        data[previous + 1] = data[previous]
                    previous -= 1
                start_index += 1

    for j in range(start_index, len(data)):
        current = data[j]
        previous = j - 1
        while previous >= start_index and data[previous] > current:
            data[previous + 1] = data[previous]
            previous -= 1
        data[previous + 1] = current

    return data


def main(data, data_template):
    print(*template_sort(data, data_template))


if __name__ == '__main__':
    # n = int(input())
    data = list(map(int, input().split()))
    # m = int(input())
    data_template = list(map(int, input().split()))
    main(data, data_template)
