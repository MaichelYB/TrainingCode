'''
Given an integer n, return all the structurally unique BST's (binary search trees), 
which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Example 1:

Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:

Input: n = 1
Output: [[1]]

Constraints:

1 <= n <= 8
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorder(self, root):
        if root != None:
            print(root.key, end = " " )
            preorder(root.left)
            preorder(root.right)
    
    def constructTrees(self, start, end):
        list = []
        """ if start > end then subtree will be
            empty so returning None in the list """
        if start > end:

            list.append(None)
            return list

        """ iterating through all values from
            start to end for constructing
            left and right subtree recursively """
        for i in range(start, end + 1):

            """ constructing left subtree """
            leftSubtree = self.constructTrees(start, i - 1)

            """ constructing right subtree """
            rightSubtree = self.constructTrees(i + 1, end)

            """ now looping through all left and
                right subtrees and connecting
                them to ith root below """
            for j in range(len(leftSubtree)) :
                left = leftSubtree[j]
                for k in range(len(rightSubtree)):
                    right = rightSubtree[k]
                    node = TreeNode(i)   # making value i as root
                    node.left = left    # connect left subtree
                    node.right = right    # connect right subtree
                    list.append(node)    # add this tree to list
        return list
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.constructTrees(1, n)