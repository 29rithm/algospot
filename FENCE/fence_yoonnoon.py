import unittest


class FenceElement:

    def __init__(self, start, height):
        self.start = start
        self.height = height

    def get_area(self, end):
        return (end-self.start) * self.height

    __slots__ = ('start', 'height',)


class Fence:

    def __init__(self, _n, _data):
        self.n = _n
        self.data = _data
        self.stack = []
        self.memo = []

    def solution(self):
        prev = -1
        for idx in range(self.n):
            height = self.data[idx]

            if prev > height:
                back = 0
                while True:
                    e = self.stack[-1]
                    if e.height > height:
                        e = self.stack.pop(-1)
                        back = e.start
                        self.memo.append(e.get_area(idx))
                        if not self.stack:
                            self.stack.append(FenceElement(e.start, height))
                            break
                    else:
                        if e.height < height:
                            self.stack.append(FenceElement(back, height))
                        break
            elif prev < height:
                self.stack.append(FenceElement(idx, height))
            else:
                pass

            prev = height

        for e in self.stack[::-1]:
            self.memo.append(e.get_area(self.n))

        self.memo.sort(reverse=True)
        return self.memo.pop(0)


def main():
    tc = input()

    for i in range(int(tc)):
        n = int(input())
        data = [int(i) for i in input().split(' ')]
        print(Fence(n, data).solution())


if __name__ == '__main__':
    main()


class Test(unittest.TestCase):

    def test_case1(self):
        test_data = [7, 1, 5, 9, 6, 7, 3, 3, 3, 3, 3, 3]
        test_n = len(test_data)
        self.assertEqual(Fence(test_n, test_data).solution(), 30)

    def test_case2(self):
        test_data = [1, 4, 4, 4, 4, 1, 1]
        test_n = len(test_data)
        self.assertEqual(Fence(test_n, test_data).solution(), 16)

    def test_case3(self):
        test_data = [1, 8, 2, 2]
        test_n = len(test_data)
        self.assertEqual(Fence(test_n, test_data).solution(), 8)

    def test_case4(self):
        test_data = [5, 4, 3, 2, 1, 99]
        test_n = len(test_data)
        self.assertEqual(Fence(test_n, test_data).solution(), 99)
