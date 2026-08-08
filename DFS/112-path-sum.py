"""
Problem Description:
Given the root of a binary tree and a target sum, return
True if there exists a root-to-leaf path whose node values
sum to the target sum.

Approach:
- Use an explicit stack to perform iterative DFS.
- Store each node along with the remaining target sum
  required after reaching that node.
- For each node:
  - If it is a leaf and the remaining sum is 0, return True.
  - Otherwise, push its children with their updated
    remaining sums.
- If all root-to-leaf paths are exhausted, return False.

Time Complexity:
O(n)

Reason:
- Every node is visited at most once.
- Each node performs only constant-time operations.

Space Complexity:
O(h)

Reason:
- h is the height of the tree.
- The DFS stack stores nodes along the active traversal.
- Worst case: O(n) for a skewed tree.
- For a balanced tree, the stack uses O(log n) space.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False

        stack = []
        stack.append([root, targetSum - root.val])

        while stack:

            element = stack.pop()
            node = element[0]
            curr = element[1]

            if not node.left and not node.right and curr == 0:
                return True
            if node.right:
                stack.append([node.right, curr-node.right.val])
            if node.left:
                stack.append([node.left, curr-node.left.val])
        return False
