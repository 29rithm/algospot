# BOARDCOVER
cards = [[(0, 0), (1, 0), (0, 1)], [(0, 0), (1, 0), (1, 1)], [(0, 0), (0, 1), (1, 1)], [(0, 0), (1, 0), (1, -1)]]
board = []


def count_board(blank_count):
    global count

    if blank_count % 3 != 0:
        return

    # find first index
    first_free = (-1, -1)
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                first_free = (row, col)
                break
        if first_free != (-1, -1):
            break

    if first_free == (-1, -1):
        count += 1
        return

    # put card on board
    for card in cards:
        if covered(first_free, card, 1):
            count_board(blank_count - 3)
        covered(first_free, card, -1)


def covered(location, card, action):
    result = True
    for ele in card:
        row = location[0] + ele[0]
        col = location[1] + ele[1]
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            result = False
            continue
        if board[row][col] == 1:
            result = False
        board[row][col] += action
    return result


if __name__ == '__main__':
    global count
    cases = int(input())
    for case in range(cases):
        board = []
        count = 0
        blank_count = 0
        size = list(map(int, input().split()))
        height, width = size[0], size[1]
        for row in range(height):
            new_row = [int(i.replace('#', '1').replace('.', '0')) for i in input()]
            board.append(new_row)
            blank_count += new_row.count(0)
        count_board(blank_count)
        print(count)
