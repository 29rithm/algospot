class Solution:
    def maxSubArray(self, nums):
        length = len(nums)

        max = nums[0]
        for i in range(length):
            sum = nums[i]

            if sum > max:
                max = sum

            for j in range(i+1, length):
                sum += nums[j]
                
                if sum > max:
                    max = sum
        return max
