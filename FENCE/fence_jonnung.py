from collections import defaultdict


def calculate_rectangle_size(width, boards):
    max_height = 0
    same_heights_indies = defaultdict(list)

    for i, v in enumerate(boards):
        height = v

        if v == 0:
            continue

        if i in same_heights_indies[v]:
            continue

        for j in range(i+1, width):
            if v <= boards[j]:
                height += v
                if v == boards[j]:
                    same_heights_indies[v].append(j)
            else:
                break

        for k in range(i-1, -1, -1):
            if v <= boards[k]:
                height += v
                if v == boards[k]:
                    same_heights_indies[v].append(k)
            else:
                break

        if height > max_height:
            max_height = height

    return max_height


if __name__ == '__main__':
    import sys

    rl = lambda: sys.stdin.readline()
    c = int(rl())
    for _ in range(c):
        n = int(rl())
        boards = list(map(int, rl().split()))
        print(calculate_rectangle_size(n, boards))