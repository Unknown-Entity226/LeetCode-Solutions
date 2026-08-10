"""
Problem Description:
Given the root of a binary tree, return its zigzag level
order traversal.

The first level is traversed from left to right, the next
level from right to left, and the direction alternates for
each level.

Approach:
- Use BFS with a queue to process the tree level by level.
- Use a NULL marker to detect the end of each level.
- Store the current level in temp.
- If the current direction is left-to-right, append temp
  directly.
- If the current direction is right-to-left, append the
  reversed temp.
- Toggle the traversal direction after every level.

Time Complexity:
O(n)

Reason:
- Every node is visited exactly once.
- Reversing each level takes O(k), where k is the size of
  that level.
- The sum of all level sizes is n, so the total reversal
  cost is O(n).

Space Complexity:
O(n)

Reason:
- The queue can contain O(n) nodes in the widest level.
- The output and temporary level list also store O(n)
  values.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        
        ans = []
        if not root:
            return ans
        temp = []
        ltr = True
        q = deque([root, None])

        while q:
            element = q.popleft()

            if not element:

                if q:

                        q.append(None)
                        if ltr:
                            ans.append(temp)
                        else:
                            ans.append(temp[::-1])
                        
                        temp =[]

                        ltr = not ltr
            else:

                    temp.append(element.val)

                    if element.left:
                        q.append(element.left)
                    if element.right:
                        q.append(element.right)
        if ltr:
            ans.append(temp)
        else:
            ans.append(temp[::-1])
        return ans
