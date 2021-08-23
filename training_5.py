# Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.

# https://leetcode.com/problems/longest-palindromic-substring/

# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Input: s = "cbbd"
# Output: "bb"

# Input: s = "a"
# Output: "a"

# Input: s = "ac"
# Output: "a"

class Solution:
  def longestPalindrome(self, s: str) -> str:
    dp = [[False for i in range(len(s))] for i in range(len(s))]
    print(dp)
    for i in range(len(s)):
      dp[i][i] = True
    max_length = 1
    start = 0
    for l in range(2,len(s)+1):
      for i in range(len(s)-l+1):
        end = i+l
        if l==2:
          if s[i] == s[end-1]:
            dp[i][end-1]=True
            max_length = l
            start = i
          else:
            if s[i] == s[end-1] and dp[i+1][end-2]:
              dp[i][end-1]=True
              max_length = l
              start = i
      return s[start:start+max_length]