"""
Problem Description:
Given the head of a linked list, reverse the nodes in
groups of size k.

- If the remaining number of nodes is less than k,
  leave them unchanged.
- Only the links between nodes may be modified.

Approach:
- Compute the length of the linked list once.
- Recursively process the list:
    - If fewer than k nodes remain, return the current
      head without modification.
    - Reverse the first k nodes iteratively.
    - Recursively reverse the remaining list using the
      updated remaining length.
    - Connect the tail of the reversed group to the
      head returned by the recursive call.
- Return the head of the reversed group.

Time Complexity:
O(n)

Space Complexity:
O(n / k)
- Due to the recursive call stack.
"""
class Solution:

    def findLength(self, head: ListNode) -> int:

        size = 0

        while head:
            size += 1
            head = head.next

        return size

    def reverse(self, head: ListNode, k: int, size: int) -> ListNode:

        if head is None or size < k:
            return head

        curr = head
        prev = None
        count = 0

        while curr and count < k:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            count += 1

        head.next = self.reverse(temp, k, size - k)

        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        size = self.findLength(head)

        return self.reverse(head, k, size)
