"""
https://leetcode.com/problems/longest-palindromic-substring/
"""
import unittest


class Solution:
    """
    Runtime: 924 ms, faster than 85.15% of Python3 online submissions for Longest Palindromic Substring.
    Memory Usage: 13.8 MB, less than 22.69% of Python3 online submissions for Longest Palindromic Substring.
    """
    def longestPalindrome(self, s: str) -> str:
        if not s and len(s) == 1:
            return s

        dp = dict()
        for i, value in enumerate(s):
            candidates = list(value)

            dp_start_position = i - len(dp[i-1]) if i > 0 else -1

            if dp_start_position > 0:
                if s[dp_start_position-1] == value:
                    dp[i] = s[dp_start_position-1:i+1]
                    continue

            for j in range(len(s[dp_start_position:i+1])):
                if is_palindromic_string(s[dp_start_position+j:i+1]):
                    candidates.append(s[dp_start_position+j:i+1])
                    break

            dp[i] = elected(candidates)

        return elected(dp.values())


def is_palindromic_string(s):
    if len(s) < 2:
        return True

    if s[0] == s[-1]:
        return is_palindromic_string(s[1:len(s)-1])


def elected(candidates):
    temp = ''
    for element in candidates:
        temp = element if len(element) > len(temp) else temp
    return temp


class TestCase(unittest.TestCase):
    def test_case_1(self):
        s = "babad"
        output = ("bab", "aba")
        self.assertIn(Solution().longestPalindrome(s), output)

    def test_case_2(self):
        s = "cbbc"
        output = ("cbbc")
        self.assertIn(Solution().longestPalindrome(s), output)
