from collections import Counter

class Solution:
    minimum_steps = 0
    def jump(self, nums):
        length = len(nums)

        if len(Counter(nums).keys()) == 1:
            return length - 1

        if length == 1:
            return 0

        if length == 2:
            return 1

        destination = length - 1
        current_step = destination - 1
        widest_stride = current_step
        while widest_stride > 0:
            if current_step + nums[current_step] >= destination:
                widest_stride = current_step

            current_step -= 1
            if current_step < 0:
                destination = widest_stride
                current_step = widest_stride - 1
                self.minimum_steps += 1
        return self.minimum_steps
