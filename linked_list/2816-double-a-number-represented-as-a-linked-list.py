"""
Problem Description:
A linked list represents a non-negative integer.

Each node contains one digit and the digits are stored
from most significant to least significant.

Return the linked list after doubling the represented number.

Approach:
- Reverse the linked list so processing starts from
  the least significant digit.
- Traverse the reversed list:
    - Multiply each digit by 2.
    - Add any carry from the previous digit.
    - Store the resulting digit.
- If a carry remains after processing all nodes,
  append a new node.
- Reverse the list again to restore the original order.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

class Solution(object):

    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        def rev(head):

            curr = head
            prev = None

            while curr:

                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev

        head = rev(head)

        curr = head
        carry = 0
        prev = None

        while curr:

            product = curr.val * 2 + carry

            curr.val = product % 10
            carry = product // 10

            prev = curr
            curr = curr.next

        if carry:

            prev.next = ListNode(carry)
            prev = prev.next

        return rev(head)
