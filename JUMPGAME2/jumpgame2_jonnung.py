class Solution:
    lowest = 0
    def jump(self, nums):
        length = len(nums)
        if length == 1:
            return 0

        if length == 2:
            return 1

        if length == sum(nums):
            return length - 1

        dst = length - 1
        current = dst - 1
        biggest = current
        while biggest > 0:
            if current + nums[current] >= dst:
                biggest = current

            current -= 1
            if current < 0:
                dst = biggest
                current = biggest - 1
                self.lowest += 1
        return self.lowest
