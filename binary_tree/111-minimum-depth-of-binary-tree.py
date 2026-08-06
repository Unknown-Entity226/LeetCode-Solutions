"""
Problem Description:
Given the root of a binary tree, return its minimum
depth, i.e., the number of nodes along the shortest path
from the root to the nearest leaf node.

Approach:
- Use recursion to compute the minimum depth of the left
  and right subtrees.
- If the current node is NULL, return 0.
- If both children exist, return 1 plus the smaller of
  the two subtree depths.
- If only one child exists, the path must continue
  through that child.
- If the node is a leaf, return 1.

Time Complexity:
O(n)

Reason:
- Every node is visited exactly once.

Space Complexity:
O(h)

Reason:
- h is the height of the tree.
- The recursion stack stores at most one call per level.
- Worst case: O(n) for a skewed tree.
- Best case: O(log n) for a balanced tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.minDepth(root.left)
        right =  self.minDepth(root.right)

        if (not left and not right) or (left and right):
            return min(left, right)+1
        else:
            return 1+max(left, right)
