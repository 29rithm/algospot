from LONGEST_PALINDROMIC_SUBSTRING.lps_jonnung import Solution


def test_lps_default_testcase():
  tc = [
    ("babad", "bab"),
    ("cbbd", "bb"),
  ]

  solution = Solution()
  for input, output in tc:
    assert solution.longestPalindrome(input) == output


def test_lps_base_case():
  tc = "a"
  assert Solution().longestPalindrome(tc) == "a"


def test_lps_no_palindronmic():
  tc = "ab"
  assert Solution().longestPalindrome(tc) == "a"


def test_lps_empty_string():
  tc = ""
  assert Solution().longestPalindrome(tc) == ""


def test_lps_twice_equal():
  tc = "bb"
  assert Solution().longestPalindrome(tc) == "bb"


def test_lps_all_equal():
  tc = "aaaa"
  assert Solution().longestPalindrome(tc) == "aaaa"


def test_lps_abcba():
  tc = "abcba"
  assert Solution().longestPalindrome(tc) == "abcba"


def test_lps_abb():
  tc = "abb"
  assert Solution().longestPalindrome(tc) == "bb"


def test_lps_abcda():
  tc = "abcda"
  assert Solution().longestPalindrome(tc) == "a"

def test_lps_aaabaaaa():
  tc = "aaabaaaa"
  assert Solution().longestPalindrome(tc) == "aaabaaa"