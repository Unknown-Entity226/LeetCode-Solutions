"""
Problem Description:
Given a perfect binary tree, populate each node's next pointer
to point to its immediate right neighbor at the same level.
The rightmost node of each level must point to None.

Approach:
- Return None if the tree is empty.
- Use a queue to perform breadth-first traversal.
- Track the number of nodes expected at the current level using total.
- Track the number of nodes already processed at the level using count.
- Connect each node to the next queued node until the rightmost
  node of the current level is reached.
- Double total and reset count when a level is completed.
- Add each node's children to the queue.
- Return the root.

Time Complexity:
O(n)

Reason:
- Each of the n nodes is removed from the queue exactly once.
- Each node requires constant-time processing.
- Queue insertion and removal take O(1) time per operation.
- Therefore, the overall time complexity is O(n).

Space Complexity:
O(n)

Reason:
- The queue stores nodes awaiting processing.
- Its maximum size is proportional to the number of nodes
  on the last level, which is O(n) in the worst case.
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        from collections import deque

        q = deque([root])

        total = 1
        count = 0
        while q:
            node = q.popleft()

            if count<total-1:
                node.next = q[0]
                count+=1
            elif count == total-1:
                total = total*2
                count = 0
            if node:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root
