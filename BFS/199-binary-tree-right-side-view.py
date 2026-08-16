"""
Problem Description:
Given the root of a binary tree, return the values of the
nodes visible from the right side of the tree, ordered from
top to bottom.

Approach:
- Perform BFS level by level using a queue.
- Store every node's value in the current level.
- Since BFS processes each level from left to right, the
  last value stored in the level is the rightmost node.
- Add the last value of every level to the answer.

Time Complexity:
O(n)

Reason:
- Every node is visited exactly once.

Space Complexity:
O(n)

Reason:
- The queue can contain O(n) nodes in the widest level.
- The temporary level list can also contain O(n) nodes.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []

        if not root:
            return ans

        from collections import deque

        q = deque([root, None])
        temp =[]
        while q:

            node = q.popleft()

            if not node:

                if q:
                    q.append(None)
                    ans.append(temp[-1])
                    temp = []

            else:

                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
        
        ans.append(temp[-1])
        return ans
