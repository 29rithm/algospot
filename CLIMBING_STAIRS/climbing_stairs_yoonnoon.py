"""
https://leetcode.com/problems/climbing-stairs/
"""
import unittest


class Solution:
    """
    Runtime: 20 ms, faster than 96.68% of Python3 online submissions for Climbing Stairs.
    Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Climbing Stairs.
    """
    def climbStairs(self, n: int) -> int:
        dp = {}
        for i in range(n):
            dp[i] = dp[i-1] + dp[i-2] if i > 1 else (1 if i == 0 else 2)
        return dp[n-1]


class TestCase(unittest.TestCase):

    def testcase_1(self):
        n = 2
        output = 2
        self.assertEqual(Solution().climbStairs(n), output)

    def testcase_2(self):
        n = 3
        output = 3
        self.assertEqual(Solution().climbStairs(n), output)

    def testcase_3(self):
        n = 45
        output = 1836311903
        self.assertEqual(Solution().climbStairs(n), output)