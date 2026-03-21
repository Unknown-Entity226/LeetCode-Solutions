'''
Problem Description:
Given the root of a Binary Search Tree (BST) and an integer key,
delete the node with value equal to the key from the BST.

Return the root of the BST after deletion.

The deletion process consists of two stages:
1. Search for the node with the given key.
2. If found, delete the node while preserving the BST property.

Approach:
- Traverse the tree using the BST property:
    - If key < root.val → search in the left subtree.
    - If key > root.val → search in the right subtree.

- When the node is found, handle three cases:

  Case 1: Node has no left child
      → Return the right child.

  Case 2: Node has no right child
      → Return the left child.

  Case 3: Node has two children
      → Find the inorder successor (smallest node in the right subtree).
      → Replace the current node's value with the successor's value.
      → Delete the successor node from the right subtree.

- Return the updated subtree root after modifications.

Time Complexity:
O(h), where h is the height of the BST.
Worst case: O(n) if the tree is skewed.

Space Complexity:
O(h) due to recursion stack.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """

        if root is None:
            return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        else:
            # Node to delete found

            # Case 1: No left child
            if root.left is None:
                return root.right

            # Case 2: No right child
            if root.right is None:
                return root.left

            # Case 3: Two children
            temp = root.right
            while temp.left is not None:
                temp = temp.left

            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)

        return root
