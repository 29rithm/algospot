class Solution:
    def __init__(self):
        self._max_length = 0
        self._searched_numbers = set()

    def lengthOfLIS(self, nums):
        self._search_lis(nums)
        return self._max_length

    def _search_lis(self, sequence_data):
        if len(sequence_data) == 1 or self._is_increasing_subsequence(sequence_data):
            candiate_cnt = len(set(sequence_data))

            if candiate_cnt > self._max_length:
                self._max_length = candiate_cnt

            return sequence_data

        for index in range(len(sequence_data)):
            if index >= (len(sequence_data)-1):
                continue

            if sequence_data[index] == sequence_data[index+1]:
                sequence_data.pop(index)

        if self._is_decreasing_subsequence(sequence_data):
            if not self._max_length:
                self._max_length = 1

            return sequence_data

        for index, number in enumerate(sequence_data):
            sequence_data.pop(index)
            search_numbers = " ".join(map(str, sequence_data))

            if search_numbers in self._searched_numbers:
                self._searched_numbers.add(search_numbers)
                sequence_data.insert(index, number)
                continue

            self._searched_numbers.add(search_numbers)
            self._search_lis(sequence_data)
            sequence_data.insert(index, number)

        return sequence_data

    def _is_increasing_subsequence(self, sequence_data):
        for index in range(len(sequence_data)):
            if index == 0:
                continue

            if sequence_data[index] < sequence_data[index - 1]:
                return False

        return True

    def _is_decreasing_subsequence(self, sequence_data):
        """
        내림차순 순열으로만 구성되어 있는가?
        """
        if len(sequence_data) == 1:
            return False

        for index in range(len(sequence_data)):
            if index == 0:
                continue

            if sequence_data[index] >= sequence_data[index - 1]:
                return False

        return True
    
if __name__ == '__main__':
    max_lis_cnt = 0
    searched_numbers = set()

    for case in range(int(input())):
        subsequence_cnt = int(input())
        subsequence = input()
        result = Solution().lengthOfLIS(subsequence.split(' '))
        print(print)

#     assert Solution().lengthOfLIS([2, 1]) == 1
#     assert Solution().lengthOfLIS([2, 2]) == 1
#     assert Solution().lengthOfLIS([2, 1, 3]) == 2
#     assert Solution().lengthOfLIS([1, 2, 3, 4]) == 4
#     assert Solution().lengthOfLIS([5, 4, 3, 2, 1, 6, 7, 8]) == 4
#     assert Solution().lengthOfLIS([5, 6, 7, 8, 1, 2, 3, 4]) == 4
#     assert Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
