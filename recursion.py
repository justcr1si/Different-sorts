# С.Ч.И.Т.А.Л.К.А с рекурсией

def counter(n, k):
    participants = list(range(1, n + 1))
    start_index = 0

    def recursive_counter(participants, k, start_index):
        if len(participants) == 1:
            return participants[0]
        index = (start_index + k - 1) % len(participants)
        participants.pop(index)
        return recursive_counter(participants, k, index)
    return recursive_counter(participants, k, start_index)


def main(n, k):
    print(counter(n, k))


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    main(n, k)
