'''
Problem Description:
Given the root of a binary tree, invert the tree and return its root.

Inverting means:
- Swap the left and right child of every node in the tree.

Approach:
- Use recursion (DFS).
- For each node:
    1. Recursively invert the left subtree.
    2. Recursively invert the right subtree.
    3. Swap the left and right children.
- Base case: if node is None, return None.

Time Complexity:
O(n), where n is the number of nodes.

Space Complexity:
O(h), where h is the height of the tree (recursion stack).
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is not None:
            self.invertTree(root.left)
            self.invertTree(root.right)
            root.left, root.right = root.right, root.left

        return root
