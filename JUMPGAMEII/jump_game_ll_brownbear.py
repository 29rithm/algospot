class Solution:
    def jump(self, nums: List[int]) -> int:
        index = 0
        cnt = 1
        length = len(nums) - 1
        if not length:
            return 0
        # 현재 인덱스와 값의 합이 길이가 넘으면 종료
        while length > index + nums[index]:
            max_value = 0
            max_index = 0
            for i in range(1, nums[index] + 1):
                # 이동할 수 있는 값에 현재 인덱스 위치인 가중치를 더함
                selectable = nums[index + i] + i
                # 최대 값이 같은 경우, 인덱스가 더 뒤에 존재할 수도 있어 equal인 경우도 포함
                if max_value <= selectable:
                    max_value = selectable
                    max_index = i
            index = index + max_index
            cnt += 1

        return cnt
