"""
yoonnoon님의 `LISv2`로 해결(외워버림)
"""
def lis_solution(sequence):
    length = len(sequence)
    memo = [1 for _ in range(length)]
    for i in range(1, length):
        for j in range(i):
            if sequence[i] > sequence[j]:
                memo[i] = max(memo[i], memo[j] + 1)

    return max(memo)


if __name__ == '__main__':
    import sys

    rl = lambda: sys.stdin.readline()

    c = int(rl())

    for _ in range(c):
        n = int(rl())
        v = list(map(int, rl().split()))
        print(lis_solution(v))