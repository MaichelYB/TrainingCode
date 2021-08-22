# Definition for singly-linked list.
# https://leetcode.com/problems/add-two-numbers/
# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def insert(self, root, item):
    # change array to linked list
    temp = ListNode(item)
    temp.data = item
    temp.next = root
    root = temp
    return root
  def lengthRecursive(self,head):
    if head is None:
      return 0
    else:
      return 1 + self.lengthRecursive(head.next)
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    result = []
    root = None
    stored = 0
    if self.lengthRecursive(l1) > self.lengthRecursive(l2):
      linked_list_used = l1
    else:
      linked_list_used = l2
    while linked_list_used:
      if l2 is None:
        result.append(l1.val)
        l1 = l1.next
      elif l1 is None:
        result.append(l2.val)
        l2 = l2.next
      else:
        result.append(l1.val + l2.val)
        l1 = l1.next
        l2 = l2.next
      linked_list_used = linked_list_used.next
    for i in range(len(result)):
      if stored > 0:
        result[i] += stored
        stored = 0
      if result[i] > 9:
        result[i] = result[i] - 10
        stored += 1
      if i == len(result) - 1 and stored > 0:
        result.append(stored)
    for i in reversed(range(len(result))):
        root = self.insert(root, result[i])
    return root