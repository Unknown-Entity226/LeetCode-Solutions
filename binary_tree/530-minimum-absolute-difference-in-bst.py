'''
Problem Description:
Given the root of a Binary Search Tree (BST),
return the minimum absolute difference between
values of any two different nodes.

Approach:
- Perform inorder traversal of the BST.
- Inorder traversal of a BST gives values in sorted order.
- The minimum absolute difference in a sorted array
  must occur between adjacent elements.

Steps:
1. Store inorder traversal values in a list.
2. Traverse adjacent pairs.
3. Compute minimum difference.

Time Complexity:
O(n), where n is the number of nodes.

Space Complexity:
O(n), for storing inorder traversal values.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        arr = []

        def traversal(root):
            if root:
                traversal(root.left)
                arr.append(root.val)
                traversal(root.right)

        traversal(root)

        diff = arr[1] - arr[0]

        for i in range(2, len(arr)):
            diff = min(diff, arr[i] - arr[i - 1])

        return diff
