class Solution:
    # Divide & Conquer
    def maxSubArray(self, nums):
        if not nums:
            return float('-inf')

        if len(nums) <= 1:
            return nums[0]

        mid = len(nums) // 2

        p_sum = 0
        left_max = 0
        for i in range(mid - 1, 0 - 1, -1):
            p_sum += nums[i]
            left_max = max(left_max, p_sum)

        p_sum = 0
        right_max = 0
        for i in range(mid + 1, len(nums), 1):
            p_sum += nums[i]
            right_max = max(right_max, p_sum)

        mid_max = left_max + right_max + nums[mid]

        return max(mid_max, self.maxSubArray(nums[:mid]), self.maxSubArray(nums[mid + 1:]))

    # DP
    def maxSubArray2(self, nums):
        total = nums[0]
        partial_sum = nums[0]
        for i in range(1, len(nums)):
            partial_sum = max(partial_sum + nums[i], nums[i])
            total = max(total, partial_sum)
        return total


if __name__ == '__main__':
    assert (Solution().maxSubArray([1])) == 1
    assert (Solution().maxSubArray([1, 2])) == 3
    assert (Solution().maxSubArray([1, -2, 2])) == 2
    assert (Solution().maxSubArray([-3, -2, -2, -3])) == -2
    assert (Solution().maxSubArray([-2, 3, 0, 2, -2, 3])) == 6
    assert (Solution().maxSubArray([-2, 3, 0, 2, -2, 3])) == 6
    assert (Solution().maxSubArray([3, 1, -2, 2, 2, 1, -2, -3])) == 7
    assert (Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])) == 6
    assert (Solution().maxSubArray([5, 8, -8, 5, -4, 2, 1, 9, 2, -8, 8, 3, -4, -5])) == 23
