result_list = []

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        score = []

        results=0
        if len(nums) == 1:
            if not result_list:
                return nums[0]
            return max(result_list)
        
        for i in range(len(nums)):
            if not score:
                score.append(nums[i])
            else:
                score.append(score[-1] + nums[i])
            if i+1 == len(nums):
                max_num = max(score)
                index = score.index(max_num) + 1
                for i in nums[:index]:
                    results += i
                if results == max_num:
                    result_list.append(results)
                nums.pop(0)
                return self.maxSubArray(nums)
