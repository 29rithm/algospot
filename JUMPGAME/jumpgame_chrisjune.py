# JUMP
# 일단 재귀적으로 본문제를 작은 부분부터 떼어내고
# 나머지 부분은 모두 메모이제이션으로 확인해보자
# 우선 특정 셀에서 갈 수 있는 곳은 두곳밖에 없다
# jump(i,j) 라는 문제가 jump(i+board[i][j],j) , jump(i,j+board[i][j])
# 이런식의 가지치기 문제가 되고 마지막에 도달할 수 있게 되면 return 끝을 내면 된다

# 기저문제, 더한 값이 밖으로 나가면 false
# 기저문제, 더한 값이 마지막 셀에 들어오면 true

# 마지막으로 연산이 반복되는 부분을 메모이제이션을 활용하여 이미 지난 곳을
# 가지 않도록처리해준다
board = []
blocked = []
def jump(row, col):
    if row >= len(board) or col >= len(board[0]):
        return False

    if blocked[row][col]==1:
        return False

    this = board[row][col]
    if this == 0:
        return True

    if jump(row, col+this) or jump(row+this, col):
        return True
    else:
        blocked[row][col] = 1

    return False

if __name__ == '__main__':
    for c in range(int(input())):
        board = []
        blocked = []
        n = int(input())
        for _ in range(n):
            board.append([int(i) for i in input().split()])
            blocked.append([0] * n)
        print('YES' if jump(0,0) else 'NO')

    # board = [[1, 1, 1], [1, 1, 1], [1, 1, 0]]
    # blocked = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    # assert jump(0,0) == True
    #
    # board = [[2, 3, 2], [3, 3, 3], [3, 3, 0]]
    # blocked = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    # assert jump(0,0) == True
    #
    # board = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,2],[1,1,1,2,0]]
    # blocked = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    # assert jump(0, 0) == False
    #
    # blocked = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
    # board = [[2,5,1,6,1,4,1],[6,1,1,2,2,9,3],[7,2,3,2,1,3,1],[1,1,3,1,7,1,2],[4,1,2,3,4,1,2],[3,3,1,2,3,4,1],[1,5,2,9,4,7,0]]
    # assert jump(0,0) == True
    #
    # blocked = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
    # board = [[2,5,1,6,1,4,1],[6,1,1,2,2,9,3],[7,2,3,2,1,3,1],[1,1,3,1,7,1,2],[4,1,2,3,4,1,3],[3,3,1,2,3,4,1],[1,5,2,9,4,7,0]]
    # assert jump(0,0) == False
    # print('Success')