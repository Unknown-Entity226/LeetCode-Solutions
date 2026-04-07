
'''
# Problem Description:
# Given the roots of two binary trees p and q,
# determine whether they are identical.
#
# Two binary trees are the same if:
# - They are structurally identical
# - Corresponding nodes have the same value

# Approach:
# - Use recursion to compare both trees simultaneously.
# - At each step:
#     1. If both nodes are None → they are equal → return True
#     2. If one is None and the other is not → return False
#     3. If values differ → return False
#     4. Recursively compare:
#         - left subtrees
#         - right subtrees
# - Return True only if both subtrees match.

# Time Complexity:
# O(n), where n is the number of nodes (we visit each node once).

# Space Complexity:
# O(h), where h is the height of the tree (recursion stack).
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if p is None and q is None:
            return True

        if p is None or q is None or p.val != q.val:
            return False

        return (
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right)
        )
