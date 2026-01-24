'''
Problem Description:
Given the head of a singly linked list, reverse the list and
return the new head of the reversed list.

Approach:
- Use three pointers to reverse the links iteratively:
  - prev: points to the previous node (initially None)
  - curr: points to the current node being processed
  - next: temporarily stores the next node
- Traverse the list:
  - Store the next node.
  - Reverse the current node’s pointer to point to prev.
  - Move prev and curr one step forward.
- After traversal, prev will point to the new head of the reversed list.

Time Complexity:
O(n), where n is the number of nodes in the linked list.'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        prev = None

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        head = prev
        return head
