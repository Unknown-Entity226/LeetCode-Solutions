"""
Problem Description:
You are given only a reference to a node in a singly linked list.

Delete that node from the linked list.

Constraints:
- You are NOT given the head of the list.
- The given node is guaranteed not to be the last node.

Approach:
Since we cannot access the previous node, we cannot
physically remove the current node.

Instead:
- Copy the value of the next node into the current node.
- Skip over the next node by updating the next pointer.

This effectively removes the next node while making the
current node appear deleted.

Time Complexity:
O(1)

Space Complexity:
O(1)
"""

class Solution(object):

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void
        """

        node.val = node.next.val
        node.next = node.next.next
