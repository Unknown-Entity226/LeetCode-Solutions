"""
Problem Description:
Given the root of a binary tree and a target sum, return
all root-to-leaf paths whose node values add up to the
target sum.

Approach:
- Use DFS with backtracking.
- Maintain the current path and the remaining target sum.
- Add the current node to the path.
- If the node is a leaf and its value equals the remaining
  sum, copy the path into the output.
- Otherwise, recursively explore the left and right
  subtrees with the updated remaining sum.
- Remove the current node from the path after exploring
  both subtrees to backtrack.

Time Complexity:
O(n × h)

Reason:
- In the worst case, O(n) nodes are visited.
- Copying a valid path into the output takes O(h),
  where h is the tree height.
- Therefore, including the cost of copying paths, the
  worst-case complexity is O(n × h).

Space Complexity:
O(h)

Reason:
- The recursion depth is at most h.
- The current path also contains at most h nodes.
- Excluding the output list.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        output =[]
        def backtrack(root, remain, path =[]):

            if not root:
                return 

            path.append(root.val)

            if not root.left and not root.right and remain== root.val:
                output.append(path[:])

            else:
                backtrack(root.left, remain-root.val, path)
            
                backtrack(root.right, remain-root.val, path)
            path.pop()

        backtrack(root, targetSum, [])
        return output
