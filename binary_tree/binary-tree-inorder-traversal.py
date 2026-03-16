'''
Problem Description:
Given the root of a binary tree, return the inorder traversal
of its nodes' values.

Inorder traversal follows the order:
      Left → Root → Right

Approach:
- Use recursion to traverse the tree.
- For each node:
    1. Recursively traverse the left subtree.
    2. Visit the current node and append its value.
    3. Recursively traverse the right subtree.
- Maintain a list to store the traversal result.

Time Complexity:
O(n), where n is the number of nodes in the tree.

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
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        inorder = []

        def traversal(inorder, root):
            if root is not None:
                traversal(inorder, root.left)
                inorder.append(root.val)
                traversal(inorder, root.right)

        traversal(inorder, root)
        return inorder
