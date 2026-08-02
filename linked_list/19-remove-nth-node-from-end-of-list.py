"""
Problem Description:
Given the head of a linked list, remove the nth node
from the end of the list and return the modified list.

Approach:
- Create a dummy node pointing to the head.
- Traverse the list once to find its length.
- Compute the index of the node to remove from the
  beginning.
- Traverse to the node just before the target node.
- Remove the target node by updating the next pointer.
- Return the list starting from dummy.next.

Time Complexity:
O(n)

Reason:
- One traversal computes the length.
- Another traversal reaches the node before the target.
- Total work is O(n).

Space Complexity:
O(1)

Reason:
- Only a few pointer variables are used.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        size = 0
        curr = head
        while curr:
            curr = curr.next
            size+=1
        
        count = size-n
        curr = dummy
        for _ in range(count):
            curr = curr.next
        
        curr.next = curr.next.next if curr.next else None

        return dummy.next
