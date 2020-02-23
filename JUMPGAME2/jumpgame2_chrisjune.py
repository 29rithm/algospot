class Solution:
    def __init__(self):
        self.jumpcnt = 0
        self.result = []

    def jump(self, nums: list) -> int:
        if len(nums) <= 1:
            self.result.append(self.jumpcnt)
            return min(self.result)

        first = nums[0]
        if first == 0:
            return

        for i in range(first):
            self.jumpcnt += 1
            self.jump(nums[i + 1:])
            self.jumpcnt -= 1
        return min(self.result)


if __name__ == '__main__':
    assert Solution().jump([2, 3, 1, 1, 4]) == 2
    assert Solution().jump([0]) == 0
    assert Solution().jump([1, 2]) == 1
    assert Solution().jump([2,3,0,1,4]) == 2
    assert Solution().jump([5,9,3,2,1,0,2,3,3,1,0,0]) == 6
    assert Solution().jump([1,1,1,1,1,1]) == 5
