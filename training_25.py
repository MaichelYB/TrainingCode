'''
https://leetcode.com/problems/generate-parentheses/
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8

'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
#         add open parenthesis if openN < n
#         add close parenthesis if open > close
        stack = []
        res = []
        
        def backtracking(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
            if openN < n:
                stack.append("(")
                backtracking(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtracking(openN, closedN + 1)
                stack.pop()
        
        backtracking(0,0)
        return res