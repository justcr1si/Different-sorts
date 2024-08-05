def sort_merge_blocks(n, data):

    blocks = 0
    max_seen = -1

    for i in range(n):
        max_seen = max(max_seen, data[i])

        if max_seen == i:
            blocks += 1

    return blocks


def main(n, data):
    print(sort_merge_blocks(n, data))


if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))
    main(n, data)
