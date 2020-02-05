class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size <= 1:
            return s

        if size == 2:
            if s[0] == s[1]:
                return s
            return s[0]

        max_str = ""
        for i in range(size):
            # abb
            l, r = i, i
            while l > 0 and r < size-1:
                l, r = l-1, r+1
                if s[l] == s[r]:
                    new_max_str = s[l:r+1]
                    if len(new_max_str) > len(max_str):
                        max_str = new_max_str
                else:
                    break

        for i in range(size):
            l, r = i, i+1
            if r < size and s[l] == s[r]:
                new_max_str = s[l:r+1]
                if len(new_max_str) > len(max_str):
                    max_str = new_max_str
            else:
                continue

            while l > 0 and r < size-1:
                l, r = l-1, r+1
                if s[l] == s[r]:
                    new_max_str = s[l:r+1]
                    if len(new_max_str) > len(max_str):
                        max_str = new_max_str
                else:
                    break

        if max_str == "":
            return s[0]

        return max_str
