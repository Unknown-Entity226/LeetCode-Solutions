"""
Problem Description:
Given the head of a linked list, detect whether a cycle exists and return
the node where the cycle begins. Return None if there is no cycle.

Approach:
- Use Floyd's Cycle Detection Algorithm with a slow and fast pointer.
- Move slow one step and fast two steps at a time.
- If they meet, a cycle exists.
- Reset slow to the head while keeping fast at the meeting point.
- Move both pointers one step at a time.
- Their next meeting point is the beginning of the cycle.
- If fast reaches None, the linked list has no cycle.

Time Complexity:
O(n)

Reason:
- The slow and fast pointers traverse the linked list a constant number of times.
- Each traversal takes at most O(n).

Space Complexity:
O(1)

Reason:
- Only a constant number of pointers are used.
- The linked list itself is not modified.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        slow = head
        
        while slow!=fast:
            slow = slow.next
            fast = fast.next

        return slow
