import unittest


class JumpGame:

    def __init__(self, _n, _data):
        self.n = _n
        self.data = _data
        self.is_arrive = False
        self.visit_memo = set()

    def solution(self):
        self.move(0, 0)
        return "YES" if self.is_arrive else "NO"

    def move(self, row, col):
        if row >= self.n or col >= self.n or (row, col) in self.visit_memo:
            return

        _next = self.data[row][col]
        if _next == 0:
            self.is_arrive = True

        if not self.is_arrive:
            self.move(row, col+_next)

        if not self.is_arrive:
            self.move(row+_next, col)

        if not self.is_arrive:
            self.visit_memo.add((row, col))


def main():
    tc = input()

    for i in range(int(tc)):
        n = int(input())
        data = []
        for j in range(n):
            data.insert(j, [int(e) for e in input().split(' ')])
        print(JumpGame(n, data).solution())


if __name__ == '__main__':
    main()


class Test(unittest.TestCase):

    def test_main(self):
        main()

    def test_case1(self):
        n = 7
        data = [
            [2, 5, 1, 6, 1, 4, 1],
            [6, 1, 1, 2, 2, 9 ,3],
            [7, 2, 3, 2, 1, 3, 1],
            [1, 1, 3, 1, 7, 1, 2],
            [4, 1, 2, 3, 4, 1, 2],
            [3, 3, 1, 2, 3, 4, 1],
            [1, 5, 2, 9, 4, 7, 0]
        ]
        self.assertEqual(JumpGame(n, data).solution(), "YES")

    def test_case2(self):
        n = 7
        data = [
            [2, 5, 1, 6, 1, 4, 1],
            [6, 1, 1, 2, 2, 9, 3],
            [7, 2, 3, 2, 1, 3, 1],
            [1, 1, 3, 1, 7, 1, 2],
            [4, 1, 2, 3, 4, 1, 3],
            [3, 3, 1, 2, 3, 4, 1],
            [1, 5, 2, 9, 4, 7, 0]
        ]
        self.assertEqual(JumpGame(n, data).solution(), "NO")

    def test_case2(self):
        n = 5
        data = [
            [1, 1, 2, 3, 3],
            [1, 1, 1, 3, 3],
            [2, 1, 1, 3, 3],
            [1, 2, 2, 3, 3],
            [1, 3, 3, 3, 0]
        ]
        self.assertEqual(JumpGame(n, data).solution(), "YES")