"""
input: 1
1


input: 2
1 1
2

input: 3
1 1 1
2 1
1 2

input: 4
1 1 1 1
2 1 1
1 2 1
1 1 2
2 2

input: 5
1 1 1 1 1
2 1 1 1
1 2 1 1
1 1 2 1
1 1 1 2
2 2 1
2 1 2
1 2 2

input: 6
1 1 1 1 1 1
2 1 1 1 1
1 2 1 1 1
1 1 2 1 1
1 1 1 2 1
1 1 1 1 2
2 2 1 1
2 1 2 1
2 1 1 2
1 2 2 1
1 2 1 2
1 1 2 2
2 2 2

input: 7
1 1 1 1 1 1 1
2 1 1 1 1 1
1 2 1 1 1 1
1 1 2 1 1 1
1 1 1 2 1 1
1 1 1 1 2 1
1 1 1 1 1 2
2 2 1 1 1
2 1 2 1 1
2 1 1 2 1
2 1 1 1 2
1 2 2 1 1
1 2 1 2 1
1 2 1 1 2
1 1 2 2 1
1 1 2 1 2
1 1 1 2 2
2 2 2 1
2 2 1 2
2 1 2 2
1 2 2 2

피보나치의 수
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        next = 0
        sum = 0
        for _ in range(n + 1):
            sum = prev + next
            prev = next
            next = sum

        return sum