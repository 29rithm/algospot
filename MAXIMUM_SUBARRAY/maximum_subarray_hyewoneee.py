class Solution:
    def __init__(self):
        self.result_list = []
        
    def maxSubArray(self, nums: List[int]) -> int:
        score = []

        results=0
        if len(nums) == 1:
            if not self.result_list:
                return nums[0]
            self.result_list.append(nums[0])
            return max(self.result_list)
        
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
                    self.result_list.append(results)
                nums.pop(0)
                return self.maxSubArray(nums)
