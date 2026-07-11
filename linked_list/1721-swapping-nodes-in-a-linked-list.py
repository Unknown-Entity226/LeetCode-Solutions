"""
Problem Description:
Given the head of a linked list and an integer k,
swap the values of:

- The kth node from the beginning.
- The kth node from the end.

Return the head of the modified linked list.

Approach:
- Traverse the list once to determine its length.
- Traverse the list again:
    - Locate the kth node from the beginning.
    - Locate the kth node from the end using the
      computed length.
- Once both nodes are found, swap their values.
- Return the head of the list.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

class Solution:

    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Find the length of the linked list
        size = 1
        curr = head

        while curr.next:
            size += 1
            curr = curr.next

        count = 1
        first = False
        second = False
        curr = head

        while curr:

            if count == k:
                temp1 = curr
                first = True

            elif count == size - k + 1:
                temp2 = curr
                second = True

            if first and second:
                temp1.val, temp2.val = temp2.val, temp1.val
                break

            count += 1
            curr = curr.next

        return head
