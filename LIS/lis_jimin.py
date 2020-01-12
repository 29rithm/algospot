def is_increasing_subsequence(sequence_data):
    for index in range(len(sequence_data)):
        if index == 0:
            continue

        if sequence_data[index] < sequence_data[index-1]:
            return False

    return True


def get_lis(sequence_data):
    global max_lis_cnt

    if len(sequence_data) == 1 or is_increasing_subsequence(sequence_data):
        candiate_cnt = len(sequence_data)

        if candiate_cnt > max_lis_cnt:
            max_lis_cnt = candiate_cnt

        return sequence_data

    for index, number in enumerate(sequence_data):
        sequence_data.pop(index)
        get_lis(sequence_data)
        sequence_data.insert(index, number)

    return sequence_data

if __name__ == '__main__':
    max_lis_cnt = 0
    searched_numbers = set()

    # for case in range(int(input())):
    #     subsequence_cnt = int(input())
    #     subsequence = input()
    #     print(get_lis(subsequence.split(' ')))

    # max_lis_cnt = 0
    # get_lis([2, 1])
    # assert max_lis_cnt == 1
    #
    # max_lis_cnt = 0
    # get_lis([2, 1, 3])
    # assert max_lis_cnt == 2
    #
    # max_lis_cnt = 0
    # get_lis([1, 2, 3, 4])
    # assert max_lis_cnt == 4
    #
    # max_lis_cnt = 0
    # get_lis([5, 4, 3, 2, 1, 6, 7, 8])
    # assert max_lis_cnt == 4
    #
    #
    # max_lis_cnt = 0
    # get_lis([5, 6, 7, 8, 1, 2, 3, 4])
    # assert max_lis_cnt == 4

    max_lis_cnt = 0
    get_lis([10, 9, 2, 5, 3, 7, 101, 18])
    assert max_lis_cnt == 4
