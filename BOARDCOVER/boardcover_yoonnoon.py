import unittest


class BoardCover:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.count = 0

    def get_lu(self, idx, board):
        """
        ##.##
        #..##
        #####
        #####
        """
        if idx // self.m == 0:
            return None
        if idx % self.m == 0:
            return None
        if board[idx - 1] == '#' or board[idx - self.m] == '#':
            return None
        return idx, idx - 1, idx - self.m

    def get_rd(self, idx, board):
        """
        #####
        ##..#
        ##.##
        #####
        """
        if idx // self.m == self.n - 1:
            return None
        if idx % self.m == self.m - 1:
            return None
        if board[idx + 1] == '#' or board[idx + self.m] == '#':
            return None
        return idx, idx + 1, idx + self.m

    def get_ru(self, idx, board):
        """
        ##.##
        ##..#
        #####
        #####
        """
        if idx // self.m == 0:
            return None
        if idx % self.m == self.m - 1:
            return None
        if board[idx + 1] == '#' or board[idx - self.m] == '#':
            return None
        return idx, idx + 1, idx - self.m

    def get_ld(self, idx, board):
        """
        #####
        #..##
        ##.##
        #####
        """
        if idx // self.m == self.n - 1:
            return None
        if idx % self.m == 0:
            return None
        if board[idx - 1] == '#' or board[idx + self.m] == '#':
            return None
        return idx, idx - 1, idx + self.m

    def solution(self, _data):
        board = ''
        for line in _data:
            board += line
        if board.count('.') % 3 != 0:
            return 0

        indices = [idx for idx in range(len(board)) if board[idx] == '.']
        self.search(list(board), indices)

        return self.count

    def search(self, board, indices):
        if board.count('.') == 0:
            self.count += 1
            return

        node = None
        for idx in indices:
            if board[idx] == '.':
                if not node:
                    node = idx
                candidates = [self.get_rd(idx, board),
                              self.get_ru(idx, board),
                              self.get_lu(idx, board),
                              self.get_ld(idx, board)]

                for element in candidates:
                    if element and node in element:
                        for _ in element:
                            board[_] = '#'
                        self.search(board, indices)
                        for _ in element:
                            board[_] = '.'


if __name__ == '__main__':
    tc = input()

    for i in range(int(tc)):
        nm = input().split(' ')
        data = (input() for row in range(int(nm[0])))
        print(BoardCover(n=int(nm[0]), m=int(nm[1])).solution(data))


class Test(unittest.TestCase):

    def test(self):
        n = 3
        m = 12
        data = (
            '####....###.',
            '#..#....##..',
            '##.#....####',
        )
        self.assertEqual(BoardCover(n, m).solution(data), 4)

    def test_case1(self):
        n = 3
        m = 7
        data = (
            '#.....#',
            '#.....#',
            '##...##',
        )
        self.assertEqual(BoardCover(n, m).solution(data), 0)

    def test_case2(self):
        n = 3
        m = 7
        data = (
            '#.....#',
            '#.....#',
            '##..###',
        )
        self.assertEqual(BoardCover(n, m).solution(data), 2)

    def test_case3(self):
        n = 8
        m = 10
        data = (
            '##########',
            '#........#',
            '#........#',
            '#........#',
            '#........#',
            '#........#',
            '#........#',
            '##########',
        )
        self.assertEqual(BoardCover(n, m).solution(data), 1514)
