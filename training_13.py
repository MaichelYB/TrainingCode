'''
https://leetcode.com/problems/3sum/
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''

from itertools import combinations
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
#         a + b + c = 0 -> a + b = -c
        arr = []
        results = []    
        if len(nums) > 0:
            for r in range(0,len(nums)+1):        
                arr += list(combinations(nums, 3))
            
            for n in arr:
                if n[0] != n[1] and n[0] != n[2] and n[1] != n[2]:
                    if n[0] + n[1] + n[2] == 0:
                        if n not in results:
                            results.append(n)
        return results