pair_list = None

n = 0
are_friends = []


def count_pairs(taken):
    first_free = -1
    for i in range(n):
        if not taken[i]:
            first_free = i
            break

    if first_free < 0:
        return 1

    ret = 0

    for pair_with in range(first_free + 1, n):
        if not taken[pair_with] and is_friend([first_free, pair_with], pair_list):
            taken[first_free] = taken[pair_with] = True
            ret += count_pairs(taken)
            taken[first_free] = taken[pair_with] = False
    return ret

def is_friend(pair, pair_list):
    for i in range(0, len(pair_list), 2):
        if (pair[0], pair[1]) == (pair_list[i], pair_list[i + 1]) or \
                (pair[0], pair[1]) == (pair_list[i + 1], pair_list[i]):
            return True
    return False


# Main
if __name__ == '__main__':
    for case in range(int(input())):
        info = list(map(int, input().split()))
        # 4
        n = info[0]
        students = [False for i in range(n)]
        # 6
        pair_count = info[1]
        pair_list = list(map(int, input().split()))
        print(count_pairs(students))
