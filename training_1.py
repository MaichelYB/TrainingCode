# Add two numbers as a linked list
# https://www.techseries.dev/daily

# You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def insert(self, root, item):
    # change array to linked list
    temp = ListNode(item)
    temp.data = item
    temp.next = root
    root = temp
    return root
    
  def addTwoNumbers(self, l1, l2, c = 0):
    # Fill this in.
    result = []
    root = None
    stored = 0
    while l1:
      temp = l1.val + l2.val
      l1 = l1.next
      l2 = l2.next
      if temp > 9:
        temp = c
        stored += 1
        result.append(temp)
        continue
      result.append(temp + stored)
      stored = 0
    # return result
    for i in reversed(range(len(result))):
      root = self.insert(root, result[i])
    return root
    

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
# print(result)
while result:
  print(result.val)
  result = result.next