class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [0 for _ in range(n)]
        for i in range(n):
            mem[i] = mem[i-1] + mem[i-2] if i > 1 else i + 1
        return mem[n-1] if n > 0 else 0


class FullSearchSolution:
    def recv(self, current, prev, goal):
        temp_sum = current + prev
        if temp_sum == goal:
            self.count += 1

        if temp_sum < goal:
            self.recv(1, temp_sum, goal)
            self.recv(2, temp_sum, goal)
        
    def climbStairs(self, n: int) -> int:
        self.count = 0
        self.recv(1, 0, n)
        self.recv(2, 0, n)
        return self.count