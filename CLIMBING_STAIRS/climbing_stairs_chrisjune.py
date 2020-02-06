class Solution:
    cache = []

    def climbStairs(self, n: int) -> int:
        if not self.cache:
            self.cache = [0 for _ in range(n+1)]

        if n in [0, 1]:
            return 1

        if self.cache[n]:
            return self.cache[n]

        self.cache[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.cache[n]


if __name__ == '__main__':
    assert Solution().climbStairs(2) == 2
    assert Solution().climbStairs(3) == 3
