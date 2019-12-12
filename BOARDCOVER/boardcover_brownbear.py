"""
흰 칸 3칸 짜리인 L자로 모든 판을 덮는 수 (회전 가능)

테스트 케이스
행 열 (H W) (1 <= H,W <= 20)
다음 H 줄에 W 수 만큼 # 과 .
#은 검은 칸, .은 흰 칸
총 흰 칸의 수는 50을 넘지 않음
3
3 7
#.....#
#.....#
##...##
3 7
#.....#
#.....#
##..###
8 10
##########
#........#
#........#
#........#
#........#
#........#
#........#
##########

결과
0
2
1514
"""


"""
3칸짜리 L 모양을 탐색하는 방법은 총 8가지다
- 알파벳 순서로 탐색을 진행한다
- 탐색 순서는 오른쪽, 아래, 왼쪽
- 위에서부터 진행하므로 위로 올라가는 길을 찾을 필요는 없다

1.
a b
  c

2.
a b
c

3. 
a
b c

# 현재 행,열의 인덱스에서 오른쪽 한 칸이 막힌 의미
4.
  a
c b

:
위에서 찾은 방법으로 진행하면서 색칠한다.


pseudo code

global 색칠된 2차원배열[행H][열W] : #은 True, .은 False로 변경
global cnt

def run(현재 행 인덱스: i, 현재 열 인덱스: j):
    if j > W:
        run(i, 0)
    if i > H:
        if 색칠된 2차원배열[행H][열W] 의 모든 값이 True인 경우:
             cnt += 1
    
    # 위 케이스 1번 확인
    if not (색칠된 2차원배열[i][j] and 색칠된 2차원배열[i][j+1] and 색칠된 2차원배열[i+1][j+1]):
        색칠된 2차원배열[i][j], 색칠된 2차원배열[i][j+1], 색칠된 2차원배열[i+1][j+1] = True
        run(i, j + 2)
    # 위 케이스 2번 확인
    if not (색칠된 2차원배열[i][j] and 색칠된 2차원배열[i][j+1] and 색칠된 2차원배열[i+1][j]):
        색칠된 2차원배열[i][j], 색칠된 2차원배열[i][j+1], 색칠된 2차원배열[i+1][j] = True
        run(i, j + 2)
    # 위 케이스 3번 확인
    if not (색칠된 2차원배열[i][j] and 색칠된 2차원배열[i+1][j] and 색칠된 2차원배열[i+1][j+1]):
        색칠된 2차원배열[i][j], 색칠된 2차원배열[i+1][j], 색칠된 2차원배열[i+1][j+1] = True
        run(i, j + 1)
    # 위 케이스 4번 확인
    if not (색칠된 2차원배열[i][j] and 색칠된 2차원배열[i+1][j] and 색칠된 2차원배열[i+1][j-1]):
        색칠된 2차원배열[i][j], 색칠된 2차원배열[i+1][j], 색칠된 2차원배열[i+1][j-1] = True
        run(i, j + 2)
    
    return cnt
    

"""


def is_success(board):
    for b in board:
        if False in b:
            return False
    return True


def run(i, j):
    global cnt
    if j >= W:
        run(i + 1, 0)

    if i >= H:
        if is_success(board):
            cnt += 1

    if i + 1 < H and j + 1 < W and not (board[i][j] or board[i][j + 1] or board[i + 1][j + 1]):
        board[i][j] = board[i][j + 1] = board[i + 1][j + 1] = True
        run(i, j + 2)
        board[i][j] = board[i][j + 1] = board[i + 1][j + 1] = False
    if i + 1 < H and j + 1 < W and not (board[i][j] or board[i][j + 1] or board[i + 1][j]):
        board[i][j] = board[i][j + 1] = board[i + 1][j] = True
        run(i, j + 2)
        board[i][j] = board[i][j + 1] = board[i + 1][j] = False
    if i + 1 < H and j + 1 < W and not (board[i][j] or board[i + 1][j] or board[i + 1][j + 1]):
        board[i][j] = board[i + 1][j] = board[i + 1][j + 1] = True
        run(i, j + 1)
        board[i][j] = board[i + 1][j] = board[i + 1][j + 1] = False
    if i + 1 < H and j < W and -1 < j - 1 and not (board[i][j] or board[i + 1][j] or board[i + 1][j - 1]):
        board[i][j] = board[i + 1][j] = board[i + 1][j - 1] = True
        run(i, j + 1)
        board[i][j] = board[i + 1][j] = board[i + 1][j - 1] = False
    if i < H and j < W and board[i][j]:
        run(i, j + 1)
    return cnt


for _ in range(int(input())):
    H, W = map(int, input().split(' '))
    board = [[s == '#' for s in input()] for _ in range(H)]
    cnt = 0
    print(run(0, 0))

