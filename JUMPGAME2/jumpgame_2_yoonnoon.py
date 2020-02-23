"""
https://leetcode.com/problems/jump-game-ii/
"""
import unittest
from typing import List


class Solution:

    def jump_dynamic_programming(self, nums: List[int]) -> int:
        """
        Time Limit Exceed( 90/92 pass )
        """
        dp = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            candidate = [dp[j]+1 for j in range(i) if nums[j] - (i-j) >= 0]
            dp[i] = min(candidate) if candidate else 0
        return dp[-1]

    def jump(self, nums: List[int]) -> int:
        """
        Runtime: 108 ms, faster than 35.42% of Python3 online submissions for Jump Game II.
        Memory Usage: 14.9 MB, less than 8.33% of Python3 online submissions for Jump Game II.
        """

        stack = []
        for i in range(len(nums) - 1):
            if i + nums[i] >= len(nums)-1:
                stack.append(-1)
                break

            else:
                if stack and i < stack[-1]:
                    continue

                next_position = 0
                for j in range(i, i+nums[i]+1):
                    next_position = j if j + nums[j] > next_position + nums[next_position] else next_position
                stack.append(next_position)

        return len(stack)


class TestCase(unittest.TestCase):

    def testcase_1(self):
        nums = [2, 3, 1, 1, 4]
        output = 2
        self.assertEqual(Solution().jump(nums), output)

    def testcase_2(self):
        nums = [1 for _ in range(10000)]
        output = 9999
        self.assertEqual(Solution().jump(nums), output)

    def testcase_3(self):
        nums = [2, 3, 1, 1, 4]
        output = 2
        self.assertEqual(Solution().jump_dynamic_programming(nums), output)

    def testcase_4(self):
        nums = [1 for _ in range(10000)]
        output = 9999
        self.assertEqual(Solution().jump_dynamic_programming(nums), output)
