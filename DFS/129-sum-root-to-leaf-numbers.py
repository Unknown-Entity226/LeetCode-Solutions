"""
Problem Description:
Given a binary tree containing digits from 0 to 9, each
root-to-leaf path represents a number.

Return the sum of all numbers represented by the
root-to-leaf paths.

Approach:
- Use DFS to traverse every root-to-leaf path.
- Maintain the number represented by the current path.
- For each node:
  - Shift the current number one digit to the left.
  - Add the current node's digit.
- When a leaf is reached, add the completed number to
  the total.
- Continue recursively through the left and right
  subtrees.

Time Complexity:
O(n)

Reason:
- Every node is visited exactly once.
- Each node performs constant-time arithmetic.

Space Complexity:
O(h)

Reason:
- The recursion stack can contain at most h calls,
  where h is the height of the tree.
- Worst case: O(n) for a skewed tree.
- Balanced tree: O(log n).
- Excluding the output/result storage.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        total = [0]

        def backtrack(root:Optional[TreeNode], curr, total):
            if not root:
                return 
            
            curr = curr*10 +root.val

            if not root.left and not root.right:
                total[0]+=curr
                return 
            
            else:
                backtrack(root.left, curr, total)
                backtrack(root.right, curr, total)
        
        backtrack(root, 0, total)
        return total[0]

