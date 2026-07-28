"""
Problem Description:
Given the root of a binary tree, return the bottom-up
level order traversal of its nodes' values.

Approach:
- Perform a level order traversal using BFS.
- Use a NULL marker to separate levels.
- Store each level in the answer.
- Reverse the final answer to obtain the bottom-up order.

Time Complexity:
O(n)

Reason:
- Every node is visited exactly once.
- Reversing the list of levels takes O(L), where L is the
  number of levels and L ≤ n.

Space Complexity:
O(n)

Reason:
- The queue may store an entire level of the tree.
- The output list stores all node values.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque

        q = deque([root])
        q.append(None)
        ans = []
        if not root:
            return ans
        temp = []
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
        return ans[::-1]
