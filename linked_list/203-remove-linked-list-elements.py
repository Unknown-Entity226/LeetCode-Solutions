"""
Problem Description:
Given the head of a linked list and an integer val,
remove all nodes whose value equals val.

Return the head of the modified linked list.

Approach:
- Create a dummy node pointing to head.
- Use:
    prev -> previous valid node
    curr -> current node being examined
- If curr.val equals val:
    - Skip the node by linking prev.next to curr.next.
- Otherwise:
    - Move both pointers forward.
- Return dummy.next.

The dummy node handles cases where the head itself
needs to be removed.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

class Solution(object):

    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """

        new_head = ListNode(0, head)

        curr = head
        prev = new_head

        while curr:

            if curr.val == val:

                temp = curr.next
                prev.next = temp
                curr = temp

            else:

                curr = curr.next
                prev = prev.next

        return new_head.next
