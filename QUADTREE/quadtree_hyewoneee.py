def boardcorver_list(data_list):
    # if len(board) == 1:
    #     print(board[0])
    # for i in range(len(board)):
    #     if i == 0:
    #         if isinstance(board[0], list):
    #             boardcorver(board[0])
    #     if i == 1:
    #         if isinstance(board[1], list):
    #             boardcorver(board[1])
    #     if i == 2:
    #         if isinstance(board[2], list):
    #             boardcorver(board[2])
    #     if i == 3:
    #         if isinstance(board[3], list):
    #             boardcorver(board[3])
    # else:
    #     return 'x' + board[2] + board[3] + board[0] + board[1]

def boardcorver(board):
    if len(board) == 1:
        print(board[0])

    board_list = board

    for i in range(len(board)):
        if isinstance(board[i], list):
            board_list[i] = boardcorver(board[i])

    return 'x' + board[2] + board[3] + board[0] + board[1]

if __name__ == '__main__':
    import sys
    case = sys.stdin.readline()

    if int(case) > 50:
        raise print('테스트 케이스는 50번을 넘길 수 없다.')

    for tc in range(int(case)):
        board_list = []
        data_list = input()
        if data_list == 'w' or data_list == 'b':
            print(data_list)
        else:
            for i in data_list:
                board_list.append(i)
            print(boardcorver(boardcorver_list(iter(board_list))))
