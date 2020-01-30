class Solution:
    def maxSubArray(self, nums):
        sub_array_sum = []
        max_sum = None
        total_count = len(nums)
        if total_count == 1:
            return sum(nums)

        for i in range(total_count):
            sub_array_sum.append(nums[i])
            if max_sum is None or nums[i] > max_sum:
                max_sum = nums[i]

            if i == total_count - 1:
                continue

            for j in range(i+1, len(nums)):
                sub_array = nums[i: j+1]
                sub_sum = sum(sub_array)
                if max_sum is None or sub_sum > max_sum:
                    max_sum = sub_sum
        return max_sum
