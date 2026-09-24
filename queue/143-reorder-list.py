"""
Problem Description:
Reorder a singly linked list from:
L0 -> L1 -> ... -> Ln-1 -> Ln

to:
L0 -> Ln -> L1 -> Ln-1 -> L2 -> ...

Only the links between existing nodes may be changed. Node values
must not be modified.

Approach:
- Store every node in a deque.
- Traverse the deque by taking the first node and then the last node
  alternately.
- Connect the selected nodes to construct the reordered list.
- Set the final node's next pointer to None to terminate the list.

Time Complexity:
O(n)

Reason:
- The linked list is traversed once to fill the deque.
- Every node is removed from the deque exactly once.

Space Complexity:
O(n)

Reason:
- The deque stores all n nodes of the linked list.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        from collections import deque

        q = deque()

        curr = head

        while curr:
        
            q.append(curr)
            curr = curr.next

        dummy = ListNode(0)

        curr = dummy

        while q:

            curr.next = q.popleft()
            curr = curr.next
            if q:
                curr.next = q.pop()
                curr = curr.next

        curr.next = None
        head = dummy.next
