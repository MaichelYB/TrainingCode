# Run time exceeded, need to find another solution
# https://leetcode.com/problems/next-greater-element-ii/
class Solution:
  def nextGreaterElements(self, nums: List[int]) -> List[int]:
    results = []
    temp = None
    for i in range(len(nums)):
      for j in reversed(range(len(nums))):
        if nums[j] > nums[i]:
          temp = nums[j]
        if temp != None and j == i:
          break
      temp = -1 if temp == None else temp
      results.append(temp)
      temp = None
    return results