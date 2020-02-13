from CLIMBING_STAIRS.climbing_stairs_jonnung import Solution


def test_climbling_stairs_testcase():
  tc = [
    (2, 2),
    (3, 3),
    (4, 5),
    (5, 8),
    (6, 13),
  ]

  solution = Solution()
  for input, output in tc:
    assert solution.climbStairs(input) == output
