class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for target in t:
            if len(s) and target == s[0]:
                s = s[1:]
        if len(s):
            return False
        return True


if __name__ == '__main__':
    assert Solution().isSubsequence('abc', 'ahbgdc')
    assert not Solution().isSubsequence('axc', 'ahbgdc')
