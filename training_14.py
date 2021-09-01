'''
3Sum Closest
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
 

Constraints:

3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-104 <= target <= 104
'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        output = 0
        temp = 0
        rank = 0
        r_while = 0
        for i in nums:
            j = rank + 1
            k = len(nums) - 1
            while j < k:
                results = i + nums[j] + nums[k]
                if results <= target:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                else:
                    k -= 1
                if r_while == 0:
                    output = results
                # if output == target:
                #     output = target
                #     break
                if abs(output-target) >= abs(results-target):
                    output = results
                r_while += 1
            rank += 1
        return output