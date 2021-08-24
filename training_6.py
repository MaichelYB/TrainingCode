# a little bit hard, need extra time to think about the answer
# https://leetcode.com/problems/longest-palindromic-subsequence/

'''
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
'''
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