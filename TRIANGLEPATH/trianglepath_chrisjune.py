# 입력은 삼각형이기 때문에
# n번째 줄은 n개의 개수
# n+1번째 줄은 n+1개수라는 것이 확정
# 한번 움직일때마다 아래 또는 아래오른쪽으로 움직인다
# 만약 idx = (r, c) 라면 -> (r+1, c) 또는 (r+1, c+1)이라는 의미이다
# 이 형태로 부분문제를 만든다

triangle = []
cache = []


def sum_triangle(r, c):
    if r >= len(triangle) or c >= len(triangle):
        return 0
    if cache[r][c] != -1:
        return cache[r][c]

    sum = 0
    sum += triangle[r][c]
    max_value = max(sum_triangle(r + 1, c), sum_triangle(r + 1, c + 1))
    sum += max_value
    cache[r][c] = sum
    return sum


if __name__ == '__main__':
    for _ in range(int(input())):
        rows = int(input())
        triangle = []
        cache = []
        for i in range(rows):
            row = [int(i) for i in input().split()]
            triangle.append(row)
            cache.append([-1 for i in range(len(row))])
        print(sum_triangle(0, 0))
