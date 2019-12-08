# BOARDCOVER
count =0
cards = [
    [(0, 0), (1, 0), (0, 1)],
    [(0, 0), (1, 0), (1, 1)],
    [(0, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (1,-1)]
]
board = []

def count_board(r, c, blank_count):
    global count
    rows = len(board)
    cols = len(board[0])

    if blank_count == 0:
        count+=1
        print(count)

    for row in range(rows):
        for col in range(cols):
            # if col<c or row<r:
            #     continue
            if board[row][col] == '#':
                continue

            for i in range(len(cards)):
                card = cards[i]
                if 0<=row+card[1][0] <rows and 0<=row+card[2][0]<rows and 0<=col+card[1][1]<cols and 0<=col+card[2][1]<cols:
                    if board[row + card[0][0]][col + card[0][1]] == board[row + card[1][0]][col + card[1][1]] == board[row + card[2][0]][col + card[2][1]] == '.':
                        board[row + card[0][0]][col + card[0][1]] = board[row + card[1][0]][col + card[1][1]] = board[row + card[2][0]][col + card[2][1]] = '#'
                        for rowss in board:
                            print(rowss)
                        print()
                        count_board(row, col, blank_count-3)
                        board[row + card[0][0]][col + card[0][1]] = board[row + card[1][0]][col + card[1][1]] = board[row + card[2][0]][col + card[2][1]] = '.'

if __name__ == '__main__':
    # cases = int(input())
    cases = 1
    for case in range(cases):
        board = []
        blank_count = 0
        # size = list(map(int, input().split()))
        size = [8, 10]
        height, width = size[0], size[1]
        # for row in range(height):
        #     board.append(list(input()))
        board = [
            list("##########"),
            list("#........#"),
            list("#........#"),
            list("#........#"),
            list("#........#"),
            list("#........#"),
            list("#........#"),
            list("##########"),
        ]
        board = [
            list("...."),
            list("...."),
            list("...."),
        ]
        for row in board:
            blank_count += row.count('.')
        count_board(0,0, blank_count)
        print(count)
