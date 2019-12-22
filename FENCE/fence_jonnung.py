from collections import defaultdict


def calculate_rectangle_size(width, boards):
    max_rectangle_size = 0
    same_heights_indies = defaultdict(list)

    for i, v in enumerate(boards):
        height = v

        if v == 0:
            continue

        if i in same_heights_indies[v]:
            continue

        right_width_index = left_width_index = i
        for j in range(i+1, width):
            if v <= boards[j]:
                if v == boards[j]:
                    same_heights_indies[v].append(j)
            else:
                right_width_index = j - 1
                break

        for k in range(i-1, -1, -1):
            if v <= boards[k]:
                if v == boards[k]:
                    same_heights_indies[v].append(k)
            else:
                left_width_index = k + 1
                break

        rectangle_size = ((right_width_index - left_width_index) + 1) * height
        if rectangle_size > max_rectangle_size:
            max_rectangle_size = rectangle_size

    return max_rectangle_size


if __name__ == '__main__':
    import sys

    rl = lambda: sys.stdin.readline()
    c = int(rl())
    for _ in range(c):
        n = int(rl())
        boards = list(map(int, rl().split()))
        print(calculate_rectangle_size(n, boards))
