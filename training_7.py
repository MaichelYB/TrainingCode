# Run time exceeded, need to find another solution
# https://leetcode.com/problems/next-greater-element-ii/
'''
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), 
return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, 
which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]

1 <= nums.length <= 104
-109 <= nums[i] <= 109
'''
class Solution:
  def nextGreaterElements(self, nums: List[int]) -> List[int]:
    results = [0]*len(nums)
    stacked_arr = []
    for i in range(len(results)):
      results[i] = -1
    for i in range(len(results) * 2):
      num = nums[i % len(results)]
      while not len(stacked_arr) == 0 and nums[stacked_arr[-1]] < num:
        results[stacked_arr.pop()] = num
      if i < len(results):
        stacked_arr.append(i)
    return results