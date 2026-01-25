
'''Problem Description:
Given the head of a sorted singly linked list, delete all duplicates
such that each element appears only once.
Return the linked list with unique elements, maintaining sorted order.

Approach:
- Since the linked list is already sorted, duplicate values will always
  appear next to each other.
- Traverse the list using a current pointer.
- For each node:
  - If the current node’s value is equal to the next node’s value,
    skip the next node by adjusting the pointer.
  - Otherwise, move the current pointer forward.
- Continue until the end of the list.
- Return the head of the modified list.

Time Complexity:
O(n), where n is the number of nodes in the linked list.'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return head

        curr = head
        while curr is not None and curr.next is not None:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head
