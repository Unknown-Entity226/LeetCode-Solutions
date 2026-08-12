"""
Problem Description:
Given the root of a Binary Search Tree (BST) and two nodes
p and q, find their Lowest Common Ancestor (LCA).

The LCA is the lowest node that has both p and q as
descendants, where a node can also be a descendant of itself.

Approach:
- Use the BST ordering property.
- If p and q lie on opposite sides of the current root,
  or one of them is the root, the current root is the LCA.
- If both p and q are greater than the current root, move
  to the right subtree.
- If both p and q are smaller than the current root, move
  to the left subtree.

Time Complexity:
O(h)

Space Complexity:
O(h)

- h is the height of the BST.
- The recursion follows only one root-to-leaf path.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if (p.val<=root.val and q.val>=root.val) or (p.val>=root.val and q.val<=root.val):
            return root
        
        if p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
