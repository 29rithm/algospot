import unittest


class TreeNode:
    def __init__(self, _value):
        self.value = _value
        self.child = [None, None, None, None]

    def __str__(self):
        return self.value + str(self.child[2]) + str(self.child[3]) + str(self.child[0]) + str(self.child[1])


class QuadTree:

    def __init__(self, _data):
        self.data = _data
        self.temp = list(self.data)
        self.root = None

    def solution(self):
        if self.data.startswith('x'):
            self.root = TreeNode(self.temp.pop(0))
            self.make_tree(self.root)
        else:
            return self.data

        return str(self.root)

    def make_tree(self, tree):
        for idx in range(len(tree.child)):
            c = self.temp.pop(0)
            if c == 'x':
                tree.child[idx] = TreeNode(c)
                self.make_tree(tree.child[idx])
            else:
                tree.child[idx] = c


if __name__ == '__main__':
    tc = input()

    for i in range(int(tc)):
        data = input()
        print(QuadTree(data).solution())


class Test(unittest.TestCase):

    def test_case1(self):
        test_data = 'w'
        self.assertEqual(QuadTree(test_data).solution(), 'w')

    def test_case2(self):
        test_data = 'xbwwb'
        self.assertEqual(QuadTree(test_data).solution(), 'xwbbw')

    def test_case3(self):
        test_data = 'xbwxwbbwb'
        self.assertEqual(QuadTree(test_data).solution(), 'xxbwwbbbw')

    def test_case4(self):
        test_data = 'xxwwwbxwxwbbbwwxxxwwbbbwwwwbb'
        self.assertEqual(QuadTree(test_data).solution(), 'xxwbxwwxbbwwbwbxwbwwxwwwxbbwb')
