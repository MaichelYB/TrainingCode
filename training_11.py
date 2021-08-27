'''
https://leetcode.com/problems/container-with-most-water/
Container With Most Water
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1
Example 3:

Input: height = [4,3,2,1,4]
Output: 16
Example 4:

Input: height = [1,2,1]
Output: 2
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
         # This variable will store the maximum area
        max_area = -maxsize
        # Left and right pointers
        left = 0
        right = len(height) - 1
        # Loop until the two pointers meet
        while left < right:
            # Shorter of the two lines
            shorter_line = min(height[left], height[right])
            max_area = max(max_area, shorter_line * (right - left))
            # If there is a longer vertical line present
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
# OOM
# class Solution:
#   def maxArea(self, height: List[int]) -> int:
#     maximum = 0
#     for i in range(len(height)):
#       for j in range(i + 1, len(height)):
#         current = j - i
#         height_curr = min(height[i], height[j])
#         maximum = max(maximum, height_curr * current)
#     return maximum