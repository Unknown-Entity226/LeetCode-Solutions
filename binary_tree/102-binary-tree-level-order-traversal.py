"""
Problem Description:
Given the root of a binary tree, return its level order
traversal, where nodes are visited level by level from
left to right.

Approach:
- Use a queue to perform BFS.
- Insert a NULL marker after each level.
- Process nodes until a NULL marker is encountered.
- Store all node values of the current level.
- Repeat until the queue becomes empty.

Time Complexity:
O(n)

Reason:
- Every node is visited exactly once.
- Each node is added to and removed from the queue once.

Space Complexity:
O(n)

Reason:
- The queue may store an entire level of the tree.
- The output list stores all n node values.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        from collections import deque

        q = deque([root])
        q.append(None)
        ans = []
        temp = []
        if not root:
            return ans
        while q:
            element = q[0]
            q.popleft()
            if not element:
                
                if q:
                    q.append(None)
                    ans.append(temp)
                    temp=[]
            else:

                temp.append(element.val)
                if element.left:
                    q.append(element.left)
                if element.right:

                    q.append(element.right)
        ans.append(temp)
        return ans
