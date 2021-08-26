'''
ZigZag Conversion
https://leetcode.com/problems/zigzag-conversion/
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
'''

class Solution:
  def convert(self, s: str, numRows: int) -> str:
    results = ['']*numRows
    total_len_1_row = numRows + numRows - 2
    max_num = total_len_1_row // 2
    pos = 0
    is_reverse = False
    results[0] = s[0]
    if numRows > len(s) - 1:
      return s
    if numRows < 2:
      return s
    for i in range(1, len(s)):
      if pos == 0 and is_reverse == True:
        is_reverse = False
      if pos == max_num:
        is_reverse = True
      if pos < max_num and is_reverse == False:
        results[pos + 1] += s[i]
        pos += 1
      elif pos == max_num and is_reverse == True:
        results[pos - 1] += s[i]
        pos -= 1
      elif pos < max_num and is_reverse == True:
        results[pos - 1] += s[i]
        pos -= 1
    return ''.join(results)