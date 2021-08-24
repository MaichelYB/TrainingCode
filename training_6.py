# a little bit hard, need extra time to think about the answer
# https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution:
  def count_palindrome(self, s, i, j, lookup):
    if i > j:
      return 0
    if i == j:
      return 1
    key = (i,j)
    if key not in lookup:
      if s[i] == s[j]:
        lookup['key'] = self.count_palindrome(s, i + 1, j - 1, lookup) + 2
      else:
        lookup['key'] = max(self.count_palindrome(s, i+1, j, lookup), self.count_palindrome(s, i, j-1, lookup))
    return lookup['key']
  def longestPalindromeSubseq(self, s: str) -> int:
    i = 0
    j = len(s)
    lookup = {}
    return self.count_palindrome(s, i, j - 1, lookup)