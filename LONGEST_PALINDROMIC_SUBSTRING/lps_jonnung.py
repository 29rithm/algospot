class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size == 1 or size == 0:
            return s

        if size == 2 and s[0] == s[1]:
            return s

        max = 0
        max_str = ""
        for i in range(1, size-1):
            l, r = i-1, i+1
            if s[l] == s[r]:
                n = 1
                while l > 0 and r < size-1:
                    if s[l-n] == s[r+n]:
                        n += 1
                    else:
                        break
                if n > max:
                    max = n
                    max_str = s[i-n:i+n+1]
            elif max <= 2:
                if s[i] == s[l]:
                    max = 2
                    max_str = s[l] + s[i]
                if s[i] == s[r]:
                    max = 2
                    max_str = s[i] + s[r]

        if max == 0:
            return s[0]

        return max_str
