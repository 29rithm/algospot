import unittest


class Wildcard:
    def __init__(self, regex):
        self.regex = regex
        self.asterisk_count = self.regex.count('*')

    def solution(self, data):
        data.sort()
        return [string for string in data
                if len(string) >= len(self.regex)-self.asterisk_count
                and self.is_match(self.regex, string, False)]

    def is_match(self, regex, string, asterisk):
        if not asterisk and not regex and string:
            return False

        if asterisk and not regex and string:
            return True

        if not regex and not string:
            return True

        if regex[0] == '*':
            return self.is_match(regex[1:], string, True)
        else:
            if not string:
                return False

            if asterisk:
                idx = -1
                for i in range(len(string)):
                    if regex[0] == '?':
                        if self.is_match(regex[1::], string[1+i::], False):
                            return True
                    else:
                        if i > idx:
                            idx = string.find(regex[0], i)
                            if idx > -1:
                                if self.is_match(regex[1::], string[idx+1::], False):
                                    return True
                            else:
                                return False
                return False
            else:
                return self.is_match(regex[1:], string[1:], False) \
                    if regex[0] == string[0] or regex[0] == '?' else False


def main():
    tc = input()

    for i in range(int(tc)):
        regex = input()
        data = []
        for j in range(int(input())):
            data.insert(j, input())

        results = Wildcard(regex).solution(data)
        for i in results:
            print(i)


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
