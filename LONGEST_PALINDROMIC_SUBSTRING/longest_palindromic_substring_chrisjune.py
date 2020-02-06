class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_result = ''
        for i in range(len(s)):
            max_result = max(max_result, self.calculate(s, i, i + 1), self.calculate(s, i,i), key=lambda x:len(x))
        return max_result

    def calculate(self, s, left, right):
        l, r = 0, 0
        while 0 <= left and right <=len(s) - 1:
            if s[left] == s[right]:
                l, r = left, right
                left -= 1
                right += 1
                continue
            else:
                break
        return s[l: r+1]



if __name__ == '__main__':
    # assert Solution().longestPalindrome('aba') == 'aba'
    assert Solution().longestPalindrome('xaba') == 'aba'
    assert Solution().longestPalindrome('xxaba') == 'aba'
    assert Solution().longestPalindrome('abax') == 'aba'
    assert Solution().longestPalindrome('abaxx') == 'aba'
    assert Solution().longestPalindrome('racecar') == 'racecar'
    assert Solution().longestPalindrome('cbbd') == 'bb'
