"""
https://leetcode.com/problems/maximum-subarray/
"""
import unittest

from typing import List


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        """
        My submissions

        Time complexity: O(n)
        runtime: 80 ms
        memory: 13.2 MB
        """
        dp = [0 for i in nums]
        for i, value in enumerate(nums, 0):
            dp[i] = value if i == 0 or dp[i-1] < 0 else dp[i-1] + value
        return max(dp)


class TestCase(unittest.TestCase):

    def test_case_1(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        output = 6
        self.assertEqual(Solution().maxSubArray(nums), output)
