class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0 for i in range(n + 1)]
        res[0], res[1], = 1, 1
        for i in range(2, n+1):
            res[i] = res[i - 2] + res[i - 1]
        return res[n]
