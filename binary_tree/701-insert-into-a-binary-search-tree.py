"""
Problem Description:
Given the root of a Binary Search Tree (BST) and a value,
insert the value into the BST and return the root of the
updated tree.

Approach:
- If the current node is NULL, create a new node with
  the given value.
- If the value is smaller than the current node, recurse
  into the left subtree.
- Otherwise, recurse into the right subtree.
- Connect the returned subtree back to the current node.
- Return the current node.

Time Complexity:
O(h)

Reason:
- h is the height of the BST.
- At each step, only one subtree is explored.
- Balanced BST: O(log n).
- Skewed BST: O(n).

Space Complexity:
O(h)

Reason:
- The recursion stack stores one call per level.
- Balanced BST: O(log n).
- Skewed BST: O(n).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            root = TreeNode(val)
            return root

        if root.val>val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root
