"""
Problem Description:
Convert a sorted array into a height-balanced Binary Search Tree.

Approach:
- Use the middle element of the current array range as the root.
- Recursively construct the left subtree using elements before the middle.
- Recursively construct the right subtree using elements after the middle.
- Continue until the current range becomes empty.

Time Complexity:
O(n)

Reason:
- Every element is processed exactly once to create a TreeNode.
- Finding the middle element takes O(1).

Space Complexity:
O(log n)

Reason:
- The recursion depth is O(log n) because the tree is height-balanced.
- The output tree itself requires O(n) space, but this is not counted as auxiliary space.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def treemake(start, end):

            if start>end:
                return None

            mid = (start+end)//2

            root = TreeNode(nums[mid])

            root.left = treemake(start, mid-1)
            root.right = treemake(mid+1, end)

            return root

        return treemake(0, len(nums)-1)

        
