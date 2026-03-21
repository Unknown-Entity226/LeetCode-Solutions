'''
Problem Description:
You are given the root of a Binary Search Tree (BST) and an integer val.
Find the node in the BST whose value equals val and return the subtree
rooted at that node.

If such a node does not exist, return None.

Approach:
- Use the Binary Search Tree property:
    - All values in the left subtree are smaller than the root.
    - All values in the right subtree are greater than the root.
- Start from the root:
    - If the root is None or root.val equals val, return root.
    - If val is smaller than root.val, search in the left subtree.
    - If val is greater than root.val, search in the right subtree.
- Continue recursively until the node is found or the subtree becomes empty.

Time Complexity:
O(h), where h is the height of the BST.
In the worst case (skewed tree), this becomes O(n).

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
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """

        if root is None or root.val == val:
            return root

        if root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
