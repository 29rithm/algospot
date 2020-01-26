# 7.4 fence
# 잘라낼 수 있는 최대 크기의 판자의 크기를 구하시오
# 제한 1초, 64MB의 메모리
# 입력 50케이스, 각 20000개 판자길이, 높이 10000이하
# for-loop로 돌면 총 2억

# 아이디어를 떠올리자
# 분할정복은 기본적으로 절반씩 나눌 때 nlogn의 속도로 하게됨
# 한번 서치하는 부분은 가운데를 끼고 검색하는것 나머지는 재귀문제가됨
# 가운데를 낀다는 의미는 무조건 두개를 포함하는 것

# 분할 정복을 어떻게 접근할 것인가?
# 가운데를 기준으로 왼쪽, 오른쪽, 가운데를 포함한 양쪽
# 왼쪽, 오른쪽 부분은 분할재귀를 호출하면 된다
# 문제가 되는 부분은 가운데를 포함한 부분일 것이다.


def fence(board):
    if len(board) <= 1:
        return board[0]
    mid = len(board) // 2
    left = mid - 1
    right = mid
    total_size = min(board[left], board[right]) * 2
    while 0 < left or right < len(board) - 1:
        if right < len(board) - 1 and (left == 0 or board[left - 1] <= board[right + 1]):
            right += 1
        else:
            left -= 1
        total_size = max(total_size, min(board[left:right + 1]) * (right - left + 1))
    return max(total_size, fence(board[:mid]), fence(board[mid:]))


if __name__ == '__main__':
    # board = [7, 1, 5, 9, 6, 7, 3]
    # assert fence(board) == 20
    # board = [1,4,4,4,4,1,1]
    # assert fence(board) == 16
    # board = [1,8,2,2]
    # assert fence(board) == 8
    for _ in range(int(input())):
        total_input = int(input())
        board = []
        for _ in range(total_input):
            board.append(int(input()))
        print(fence(board))
