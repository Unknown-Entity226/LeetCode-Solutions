"""
Problem Description:
Given the root of a binary tree, return its maximum
depth, i.e., the number of nodes along the longest path
from the root to a leaf.

Approach:
- Use recursion to compute the depth of the left and
  right subtrees.
- If the current node is NULL, return 0.
- Otherwise, return 1 plus the maximum of the two
  subtree depths.

Time Complexity:
O(n)

Reason:
- Every node is visited exactly once.

Space Complexity:
O(h)

Reason:
- h is the height of the tree.
- The recursion stack stores at most one call per level.
- In the worst case (skewed tree), h = n.
- In a balanced tree, h = log n.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right)+1
