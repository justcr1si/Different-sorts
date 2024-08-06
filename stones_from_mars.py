def get_amount_of_customers(n, source_data, m, real_data):
    source_data.sort()
    real_data.sort()

    i, j = 0, 0
    completed_orders = 0

    while i < n and j < m:
        if real_data[j] >= source_data[i]:
            completed_orders += 1
            i += 1
        j += 1

    return completed_orders


def main(n, source_data, m, real_data):
    print(get_amount_of_customers(n, source_data, m, real_data))


if __name__ == '__main__':
    n = int(input())
    source_data = list(map(int, input().split()))
    m = int(input())
    real_data = list(map(int, input().split()))
    main(n, source_data, m, real_data)
