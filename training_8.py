'''
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/616/week-4-august-22nd-august-28th/3918/

Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Input: c = 3
Output: false
Input: c = 4
Output: true
Input: c = 2
Output: true
Input: c = 1
Output: true

0 <= c <= 231 - 1
'''
import math
class Solution:
  def judgeSquareSum(self, c: int) -> bool:
    i = 0
    temp = 0
    while True:
      if c <= 2:
        return True
      if c - i ** 2 <= 0:
        break
      temp = math.sqrt(c - i ** 2)
      if temp.is_integer():
        break
      i += 1
    temp = temp if temp.is_integer() else 0
    results = math.sqrt(c - temp ** 2)
    return True if results.is_integer() else False

if __name__ == 'main':
  print(Solution.judgeSquareSum(30))