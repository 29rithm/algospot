# LIS = Longest Increasing Sequence
# 순 증가하는 수열을 나타낸다. 다시말하여 왼쪽에서 오른쪽으로 증가하는 숫자의 나열을 나타낸다
# 해당 문제에서는 숫자리스트가 주어지고, 리스트에서 순증가하는 수열의 최대개수를 반환하는 함수를 푸는 것이다

# [5,6,7,8,1,2,3] -> 4를 반환하는 것이다
# TC50, 입력이 500개이기 때문에 500*500*50

# def lis(seq):
#     maxcnt = 0
#     for i in range(len(seq)):
#         cnt = 1
#         for j in range(i+1, len(seq)):
#             first = seq[i]
#             second = seq[j]
#             if first < second:
#                 cnt += 1
#         maxcnt = max(maxcnt, cnt)
#     return maxcnt


def lis(seq):
    # 가운데를 포함한 녀석들을 계산
    if len(seq) <= 1:
        return 1
    mid = len(seq) // 2
    left = mid - 1
    right = mid
    max_len = 2 if seq[left] < seq[right] else 1
    l = left
    r = right

    while (0 < left or right < len(seq) - 1):
        if right < len(seq) - 1 and (left == 0 or seq[left - 1] < seq[right + 1]):
            if seq[r] < seq[right+1]:
                max_len += 1
                r += 1
            right += 1
        else:
            if seq[left-1] < seq[l]:
                max_len += 1
                l -= 1
            left -= 1
    # 가운데를 뺀 왼쪽
    return max(max_len, lis(seq[:mid]), lis(seq[mid:]))


# if __name__ == '__main__':
#     for _ in range(int(input())):
#         count = int(input())
#         seq = [int(i) for i in input().split()]
#         print(lis(seq))
if __name__ == '__main__':
    assert lis([1, 2, 3, 4]) == 4
    print(lis([1,2,3,9,4,5,6]))
    print(lis([5,6,7,8,1,2,3,4]))
    assert lis([5,6,7,8,1,2,3,4]) == 4
    assert lis([9,1,2,3,4]) == 4
    assert lis([2, 5, 6, 1, 2]) == 3
    assert lis([9, 1, 3, 7, 5, 6, 20]) == 5
