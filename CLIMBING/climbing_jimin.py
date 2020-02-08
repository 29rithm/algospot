class Solution:
    def __init__(self):
        self.climb_history = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n

        return self._climb_combination(n)

    def _climb_combination(self, n):
        if not n in self.climb_history:
            self.climb_history[n] = self._climb_combination(n-1) + self._climb_combination(n-2)

        return self.climb_history[n]

if __name__ == '__main__':
    assert Solution().climbStairs(1) == 1
    assert Solution().climbStairs(2) == 2
    assert Solution().climbStairs(3) == 3
    assert Solution().climbStairs(4) == 5
    assert Solution().climbStairs(5) == 8
    assert Solution().climbStairs(6) == 13
