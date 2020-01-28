class Solution:
    def maxSubArray(self, nums):
        if len(nums) <= 1:
            return nums[0]

        mid = len(nums)//2
        left = mid - 1
        right = mid
        total_sum = sum(nums[left:right+1])

        while 0 < left or right < len(nums)-1:
            if right < len(nums) - 1 and (left == 0 or nums[left-1] <= nums[right+1]):
                right += 1
            else:
                left -= 1
            total_sum = max(total_sum, sum(nums[left:right+1]))

        return max(total_sum, self.maxSubArray(nums[:mid]), self.maxSubArray(nums[mid:]))


if __name__ == '__main__':
    # print(Solution().maxSubArray([1,2,3]))
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))