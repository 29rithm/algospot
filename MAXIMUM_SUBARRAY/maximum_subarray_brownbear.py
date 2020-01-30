class Solution:
    def maxSubArray(self, nums):
        sequence_sum = 0
        max_sum = -9999999999999

        for num in nums:
            if sequence_sum < 0:
                sequence_sum = num
            else:
                sequence_sum += num

            if sequence_sum > max_sum:
                max_sum = sequence_sum

        return max_sum
