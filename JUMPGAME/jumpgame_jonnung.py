
class JumpGame:
    def __init__(self, width, game_board):
        self.reachable = False
        self.width = width
        self.game_board = game_board
        self.jump_history = [[0 for _ in range(width)] for _ in range(width)]

    def check_movable(self, i, j):
        move_distance = self.game_board[i][j]
        down_movable = i + move_distance < self.width
        right_movable = j + move_distance < self.width
        return down_movable, right_movable

    def right(self, i, j):
        move_distance = self.game_board[i][j]
        return i, j + move_distance

    def down(self, i, j):
        move_distance = self.game_board[i][j]
        return i + move_distance, j

    def jump(self, i=0, j=0):
        if ((i + 1) * (j + 1)) == self.width**2:
            self.reachable = True
            return True

        if self.reachable:
            return True

        if i >= self.width or j >= self.width:
            return False

        if self.jump_history[i][j] != 0:
            return self.jump_history[i][j]

        down_movable, right_movable = self.check_movable(i, j)
        if down_movable or right_movable:
            down_result = False
            right_result = False

            if down_movable:
                next_down_position = self.down(i, j)
                down_result = self.jump(*next_down_position)

            if right_movable:
                next_right_position = self.right(i, j)
                right_result = self.jump(*next_right_position)

            self.jump_history[i][j] = down_result or right_result
        else:
            self.jump_history[i][j] = False

        return self.jump_history[i][j]


if __name__ == '__main__':
    import sys

    rl = lambda: sys.stdin.readline()

    c = int(rl())

    for _ in range(c):
        n = int(rl())
        game_board = []
        for _ in range(n):
            game_board.append(list(map(int, rl().split())))

        jg = JumpGame(n, game_board)
        jg.jump()
        print("YES" if jg.reachable else "NO")
