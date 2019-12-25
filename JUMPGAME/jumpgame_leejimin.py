memorize_jump_history = {}


def has_jump_way(point, game_board):
    global memorize_jump_history

    y_point = point[0]
    x_point = point[1]

    memorize_key = ":".join(map(str, point))

    if memorize_key in memorize_jump_history:
        return memorize_jump_history[memorize_key]

    if (y_point > max_y_point) or (x_point > max_x_point):
        return False

    if x_point == max_x_point and (y_point == max_y_point):
        return True

    point_value = game_board[y_point][x_point]

    right_point = (y_point, x_point + point_value)
    right_memorize_key = ":".join(map(str, right_point))
    if has_jump_way(right_point, game_board):
        memorize_jump_history[right_memorize_key] = True
        return True
    else:
        memorize_jump_history[right_memorize_key] = False

    down_point = (y_point + point_value, x_point)
    down_memorize_key = ":".join(map(str, down_point))
    if has_jump_way(down_point, game_board):
        memorize_jump_history[down_memorize_key] = True
        return True
    else:
        memorize_jump_history[down_memorize_key] = False
        return False

    return False


if __name__ == "__main__":
    tc = input()
    result_list = []

    for i in range(int(tc)):
        memorize_jump_history = {}
        board_list = []
        board_height = int(input())

        for _ in range(board_height):
            board = [int(height) for height in input().split(" ")]
            board_list.append(board)

        max_y_point = board_height - 1
        max_x_point = len(board_list[0]) - 1

        result_list.append(has_jump_way((0, 0), board_list))

    for result in result_list:
        if result:
            print("YES")
        else:
            print("NO")
