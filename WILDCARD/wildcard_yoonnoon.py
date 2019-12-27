import unittest


class Wildcard:
    def __init__(self, regex):
        self.regex = regex

    def solution(self, data):
        pass


def main():
    tc = input()

    for i in range(int(tc)):
        regex = input()
        data = []
        for j in range(int(input())):
            data.insert(j, input())

        Wildcard(regex).solution(data)


if __name__ == '__main__':
    main()


class Test(unittest.TestCase):

    def test_main(self):
        main()

    def test_case1(self):
        regex = 'he?p'
        data = ['help', 'heap', 'helpp']
        self.assertEqual(Wildcard(regex).solution(data), ['heap', 'help'])

    def test_case2(self):
        regex = '*p*'
        data = ['help', 'papa', 'hello']
        self.assertEqual(Wildcard(regex).solution(data), ['help', 'papa'])
