'''
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.

 

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Example 3:

Input: dividend = 0, divisor = 1
Output: 0
Example 4:

Input: dividend = 1, divisor = 1
Output: 1
 

Constraints:

-231 <= dividend, divisor <= 231 - 1
divisor != 0
'''

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # MAX and MIN values for integer
        MAX = 2147483647
        MIN = -2147483648
        # Check for overflow
        if divisor == 0 or (dividend == MIN and divisor == -1):
            return MAX
        # Sign of result`
        sign = -1 if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0) else 1
        # Quotient
        quotient = 0
        # Take the absolute value
        absoluteDividend = abs(dividend)
        absoluteDivisor = abs(divisor)
        # Loop until the  dividend is greater than divisor
        while absoluteDividend >= absoluteDivisor:
            # This represents the number of bits shifted or
            # how many times we can double the number
            shift = 0
            while absoluteDividend >= (absoluteDivisor << shift):
                shift += 1
            # Add the number of times we shifted to the quotient
            quotient += (1 << (shift - 1))
            # Update the dividend for the next iteration
            absoluteDividend -= absoluteDivisor << (shift - 1)
        return -quotient if sign == -1 else quotient