class Solution:
    # def maxSubArray(self, nums):
        # if len(nums) <= 1:
        #     return nums[0]
        #
        # mid = len(nums)//2
        # left = mid - 1
        # right = mid
        # total_sum = sum(nums[left:right+1])
        #
        # while 0 < left or right < len(nums)-1:
        #     if right < len(nums) - 1:
        #         if left == 0 or nums[left-1] < nums[right+1]:
        #             right += 1
        #         elif nums[left-1] == nums[right+1]:
        #             if nums[right+1] >= 0:
        #                 right += 1
        #             else:
        #                 left_sum = self.maxSubArray(nums[:left])
        #                 right_sum = self.maxSubArray(nums[right+1:])
        #                 total_sum = max(total_sum, left_sum, right_sum)
        #                 if left_sum < right_sum:
        #                     right += 1
        #                 else:
        #                     left -= 1
        #         else:
        #             left -= 1
        #     else:
        #         left -= 1
        #     total_sum = max(total_sum, sum(nums[left:right+1]))
        #     print('NUMS', nums[left:right+1], total_sum)
        # return max(total_sum, self.maxSubArray(nums[:mid]), self.maxSubArray(nums[mid:]))

    def maxSubArray(self, nums):
        total = nums[0]
        partial_sum = nums[0]
        for i in range(1, len(nums)):
            partial_sum = max(partial_sum+nums[i], nums[i])
            total = max(total, partial_sum)
        return total


if __name__ == '__main__':
    print(Solution().maxSubArray([1]))
    assert (Solution().maxSubArray([1, -2, 2])) == 2
    assert (Solution().maxSubArray([-3,-2,-2,-3])) == -2
    assert (Solution().maxSubArray([-2,3,0,2,-2,3])) == 6
    assert (Solution().maxSubArray([-2,3,0,2,-2,3])) == 6
    assert (Solution().maxSubArray([3,1,-2,2,2,1,-2,-3])) == 7
    assert (Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) == 6
    assert (Solution().maxSubArray([5,8,-8,5,-4,2,1,9,2,-8,8,3,-4,-5])) == 23

