"""
Problem Description:
Given the head of a linked list, delete the middle node
and return the modified list.

The middle node is defined as the:

    floor(n / 2)

th node using 0-based indexing.

Examples:

    [1]       -> []
    [1,2]     -> [1]
    [1,2,3]   -> [1,3]
    [1,2,3,4] -> [1,2,4]

Approach:
- Handle lists with 0 or 1 node separately.
- Use the slow-fast pointer technique:
    - slow moves one step at a time.
    - fast moves two steps at a time.
- Keep track of the node before slow using prev.
- When fast reaches the end:
    - slow points to the middle node.
- Delete the middle node by:

      prev.next = slow.next

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

class Solution(object):

    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if head == None or head.next == None:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:

            fast = fast.next.next
            prev = slow
            slow = slow.next

        prev.next = slow.next

        return head
