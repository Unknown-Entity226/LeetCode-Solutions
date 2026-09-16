"""
Problem Description:
Given the root of a binary tree, return the sum of all left leaves.

A left leaf is a node that:
- Has no left or right child.
- Is the left child of its parent.

Approach:
- Perform an iterative DFS using a stack.
- Store each node along with a flag indicating whether it is a left
  child of its parent.
- When visiting a node, push its children onto the stack and mark the
  left child with 1 and the right child with 0.
- If the current node has no children and its left-child flag is 1,
  add its value to the answer.

Time Complexity:
O(n)

Reason:
- Every node is visited exactly once.

Space Complexity:
O(n)

Reason:
- The stack can contain O(n) nodes in the worst case.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        stack =[(root, 0)]
        ans = 0
        while stack:
            element = stack.pop()

            if element[0].left:
                stack.append((element[0].left, 1))
            if element[0].right:
                stack.append((element[0].right, 0))
            
            
            if  not element[0].left and not element[0].right and element[1] == 1:
                    ans+=element[0].val
        return ans
            
