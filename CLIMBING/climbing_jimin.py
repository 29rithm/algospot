class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0

        self.climb_history = [None for _ in range(n+1)]
        self.stairs = [None for _ in range(n)]

        return len(self._climb_combination(self.stairs))

    def _climb_combination(self, stairs):
        stairs_len = len(stairs)
        if stairs_len == 1:
            return [[1]]

        if self.climb_history[stairs_len]:
            return self.climb_history[stairs_len]

        # 한 계단 오른 경우
        one_step_combinations = self._climb_combination(stairs[1:])
        for one_step_combination in one_step_combinations:
            one_step_combination.insert(0, stairs[0])

        # 두 계단 오른 경우
        if stairs_len == 2:
            two_step_combinations = [[2]]
        else:
            two_step_combinations = self._climb_combination(stairs[2:])

        combinations = []
        for one_step_combination in one_step_combinations:
            combinations.append(one_step_combination)

        for two_step_combination in two_step_combinations:
            combinations.append(two_step_combination)

        self.climb_history[stairs_len] = combinations
        return combinations

if __name__ == '__main__':
    assert Solution().climbStairs(1) == 1
    assert Solution().climbStairs(2) == 2
    assert Solution().climbStairs(3) == 3
    assert Solution().climbStairs(4) == 5
    assert Solution().climbStairs(5) == 8
    assert Solution().climbStairs(6) == 13
