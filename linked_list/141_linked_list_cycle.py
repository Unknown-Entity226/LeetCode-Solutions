'''
Problem Description:
Given the head of a singly linked list, determine if the linked list
contains a cycle.

A cycle exists if there is a node that can be reached again by continuously
following the `next` pointer.

Note:
- The variable `pos` is used internally by the problem to represent the
  index where the tail connects, but it is NOT given as input.
- Return True if there is a cycle, otherwise return False.

Approach:
- Use Floyd’s Cycle Detection Algorithm (Tortoise and Hare).
- Initialize two pointers:
  - slow moves one step at a time.
  - fast moves two steps at a time.
- If there is a cycle, fast and slow pointers will eventually meet.
- A counter is used to ignore the initial condition where both pointers
  start at the head.
- If the pointers meet again after movement has started, a cycle exists.
- If the fast pointer reaches the end, the list has no cycle.

Time Complexity:
O(n), where n is the number of nodes in the linked list.'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        count = 0

        while fast is not None and fast.next is not None:
            if fast == slow and count:
                return True
            elif fast == slow and not count:
                count += 1

            fast = fast.next.next
            slow = slow.next

        return False
