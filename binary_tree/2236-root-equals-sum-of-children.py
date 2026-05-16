'''
Problem Description:
Given a binary tree consisting of exactly 3 nodes:
- the root
- its left child
- its right child

Return True if:
    root.val == root.left.val + root.right.val

Otherwise, return False.

Approach:
- Directly compare:
      root value
  with:
      sum of left and right child values

- Since the tree always has exactly 3 nodes,
  no null checks are required.

Time Complexity:
O(1)

Space Complexity:
O(1)
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def checkTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return root.val == (root.left.val + root.right.val)
