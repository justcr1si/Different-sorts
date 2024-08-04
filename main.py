# С.Ч.И.Т.А.Л.К.А с циклом

def counter(n, k):
    participants = list(range(1, n + 1))
    index = 0

    while len(participants) > 1:
        index = (index + k - 1) % len(participants)
        participants.pop(index)

    return participants[0]


def main(n, k):
    print(counter(n, k))


if __name__ == '__main__':
    n = int(input())        # число претендентов
    k = int(input())        # число тактов
    main(n, k)
