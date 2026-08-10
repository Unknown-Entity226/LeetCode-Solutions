"""
Problem Description:
Given a binary tree, determine whether it is height-balanced.

A binary tree is height-balanced if the difference between
the heights of the left and right subtrees of every node is
at most 1.

Approach:
- Use DFS to calculate the height and balance status of
  every subtree simultaneously.
- For each node:
  - Recursively obtain the balance status and height of
    both subtrees.
  - Check whether their height difference is at most 1.
  - The current subtree is balanced only if both child
    subtrees are balanced and the current height difference
    is at most 1.
- Return both the balance status and height.

Time Complexity:
O(n)

Reason:
- Every node is visited exactly once.
- Height is calculated during the same DFS traversal.

Space Complexity:
O(h)

Reason:
- The recursion stack contains at most h calls, where h
  is the height of the tree.
- Worst case: O(n) for a skewed tree.
- Balanced tree: O(log n).
"""
# Definition for a binary tree node.
# class TreeNode:
# def __init__(self, val=0, left=None, right=None):
# self.val = val
# self.left = left
# self.right = right
class Solution:

    def recur(self, root: Optional[TreeNode])-> tuple[bool, int]:
        if not root:
            return( True, 0)
        
        left = self.recur(root.left)
        right = self.recur(root.right)

        leftSub = left[0]
        rightSub = right[0]

        diff = abs(left[1]-right[1])<=1

        height = max(left[1],right[1])+1

        if diff and rightSub and leftSub:
            return (True, height)
        else:
            return (False, height)
            
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        ans, height = self.recur(root)

        return ans
