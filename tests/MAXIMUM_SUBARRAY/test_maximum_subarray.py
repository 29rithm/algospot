from MAXIMUM_SUBARRAY.maximum_subarray_jonnung import Solution


def test_max_subarray_base_case():
    input = [1]
    result = Solution().maxSubArray(input)
    assert result == 1

def test_max_subarray_leetcode_tc():
    input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = Solution().maxSubArray(input)
    assert result == 6

def test_max_subarray_length_two():
    input = [-2, 1]
    result = Solution().maxSubArray(input)
    assert result == 1

def test_max_subarray_length_one():
    input = [-1]
    result = Solution().maxSubArray(input)
    assert result == -1

def test_max_subarray_length_three():
    input = [1, -1, 1]
    result = Solution().maxSubArray(input)
    assert result == 1