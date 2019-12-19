def run(i, j):
    # 인덱스가 도착지점이면 True 반환. 배열에 직접 접근하는 것보다 변수와 비교하는게 조금 더 빠른거 같음
    if i == n - 1 and j == n - 1:
        return True

    is_end = False
    tile = int(board[i][j])
    # 오른쪽, 아래쪽 순으로 진행하기 때문에 한 번 방문한 타일은 이미 경우의 수를 전부 계산했기 때문에 건너 뛴다. - *이거 안 하면 시간초과*
    if tile != -1:
        if not is_end and j + tile < n:
            is_end = run(i, j + tile)
        if not is_end and i + tile < n:
            is_end = run(i + tile, j)
        # 오른쪽, 아래쪽까지 전부 이동한 상태면 현재 타일을 방문했다는 표시로 -1로 변경
        board[i][j] = -1
    return is_end


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        # 1차원 배열일 땐, list(map(int, 배열))로 먼저 형변환을 진행하는 것이 비교할 때마다 형변환을 진행하는 것보다 조금 더 빠르지만
        # 2차원 배열의 경우, 비교할 때마다 형변환을 하는 것이 map()을 사용해 미리 형변환을 하는 것보다 30% 이상 빠르다.
        # **정정** 2차원 배열을 전부 다 탐색할 때는, 형변환을 먼저 한 것이 조금 더 빠름. -> 전체 탐색이 아닌 경우는, 비교할 때마다 형변환 하는게 더 효율적
        board = [input().split() for _ in range(n)]
        print('YES' if run(0, 0) else 'NO')
