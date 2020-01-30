class Solution:
    def maxSubArray(self, nums):
        size = len(nums)

        current_max = global_max = nums[0]

        for i in range(1, size):
            current_max = max(nums[i], nums[i] + current_max)
            if current_max > global_max:
                global_max = current_max

        return global_max
