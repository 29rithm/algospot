# H x W의 카드로 덮는다
# 문제는, 카드마다 모양이 다르기 때문에 뒷셀의 카드를 먼저 덮은경우 중복으로 세게 된다.
# 따라서 카드놓는 셀을 선택할 순서를 정해놓으면 앞에서 뒤로, 뒤에서 앞으로 세는 것을 막을 수 있다.
# 그 셀을 선택하는 기준을 가장 윗쪽 오른쪽부터 찾아내고, 그 셀에 카드를 대어보고 맞으면
# 재귀를 태운다.

# 또 문제는, 카드를 놓을 수 없던 경우 놓았던 카드를 ㄱ자를 놓고 ㄴ자 모양의 다른 카드도 놓아야하기 때문에
# 카드를 놓을 수 있는 경우에는 재귀 함수 이후에 카드를 떼는 로직이 필요하고,
# 카드를 놓을 수 없는 경우에는 재귀를 태우지 않아야 한다.

cards = [
    [(0, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (1, 1)],
    [(0, 0), (1, 0), (1, -1)],
    [(0, 0), (1, 0), (0, 1)]
]


def counter(board):
    first = (-1, -1)
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                first = (row, col)
                break
        if first != (-1, -1):
            break
    if first == (-1, -1):
        return 1

    count = 0
    for card in cards:
        if covered(card, board, first, 1):
            count += counter(board)
        covered(card, board, first, -1)
    return count


# 카드가 겹치는 것과 무관하게 일단 카드를 올린다고 판단해야, rollback할 때 편하다
def covered(card, board, index, direction):
    result = True
    for idx in card:
        new_row = index[0] + idx[0]
        new_col = index[1] + idx[1]
        if new_row < 0 or new_col < 0 or new_row >= len(board) or new_col >= len(board[0]):
            result = False
            continue
        if board[new_row][new_col] != 0:
            result = False
        board[new_row][new_col] += direction
    return result


if __name__ == '__main__':
    for case in range(int(input())):
        board = []
        info = [int(i) for i in input().split()]
        for i in range(info[0]):
            board.append([1 if i == '#' else 0 for i in list(input())])
        print(counter(board))
