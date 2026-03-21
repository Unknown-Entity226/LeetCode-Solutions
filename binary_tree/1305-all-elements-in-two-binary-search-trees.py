'''
Problem Description:
Given the roots of two Binary Search Trees (BSTs),
return a list containing all the integers from both trees
in sorted (ascending) order.

Approach:
- Perform inorder traversal on both BSTs:
    - This gives two sorted lists (l1 and l2).
- Merge the two sorted lists using the two-pointer technique
  (similar to merge step in merge sort).
- Return the merged sorted list.

Time Complexity:
O(n + m), where:
  n = number of nodes in root1
  m = number of nodes in root2

Space Complexity:
O(n + m), for storing traversal results and merged list.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: List[int]
        """
        l1 = []
        l2 = []

        def traversal(root, arr):
            if root is not None:
                traversal(root.left, arr)
                arr.append(root.val)
                traversal(root.right, arr)

        traversal(root1, l1)
        traversal(root2, l2)

        i = j = 0
        result = []

        while i < len(l1) and j < len(l2):
            if l1[i] > l2[j]:
                result.append(l2[j])
                j += 1
            else:
                result.append(l1[i])
                i += 1

        while i < len(l1):
            result.append(l1[i])
            i += 1

        while j < len(l2):
            result.append(l2[j])
            j += 1

        return result
