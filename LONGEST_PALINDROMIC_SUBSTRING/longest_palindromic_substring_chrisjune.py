class Solution:
    def longestPalindrome(self, s: str) -> str:
        mid = len(s)//2
        left = mid
        right = mid
        for i in range(1, len(s)-mid):
            if s[mid-i] != s[mid+i]:
                break
            left = mid - i
            right = mid + i
        palin = s[left:right+1]

        maxstr = max(palin)
        return palin

if __name__ == '__main__':
    print(Solution().longestPalindrome('racecar'))
    assert Solution().longestPalindrome('cbbd') == 'bb'
