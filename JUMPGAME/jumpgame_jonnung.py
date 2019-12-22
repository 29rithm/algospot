
class JumpGame:
    def __init__(self, width, game_board):
        self.reachable = False
        self.width = width
        self.game_board = game_board

    def check_movable(self, i, j):
        move_distance = self.game_board[i][j]
        down_movable = i + move_distance < self.width
        right_movable = j + move_distance < self.width
        return down_movable, right_movable

    def right(self, i, j):
        move_distance = self.game_board[i][j]
        return (i, j + move_distance,), self.game_board[i][j + move_distance]

    def down(self, i, j):
        move_distance = self.game_board[i][j]
        return (i + move_distance, j,), self.game_board[i + move_distance][j]

    def jump(self, i=0, j=0):
        if ((i + 1) * (j + 1)) == self.width**2:
            self.reachable = True

        down_movable, right_movable = self.check_movable(i, j)

        if down_movable and not self.reachable:
            next_position, distance = self.down(i, j)
            self.jump(*next_position)

        if right_movable and not self.reachable:
            next_position, distance = self.right(i, j)
            self.jump(*next_position)


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
