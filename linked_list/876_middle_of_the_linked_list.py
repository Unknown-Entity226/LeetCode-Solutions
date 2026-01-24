'''
Problem Description:
Given the head of a singly linked list, return the middle node of the list.
If there are two middle nodes (i.e., the list has even length),
return the second middle node.

Approach:
- Use two pointers: a slow pointer and a fast pointer.
- Initialize both pointers at the head of the linked list.
- Move the slow pointer one step at a time.
- Move the fast pointer two steps at a time.
- When the fast pointer reaches the end of the list,
  the slow pointer will be at the middle.
- In case of an even-length list, this method naturally
  returns the second middle node.

Time Complexity:
O(n), where n is the number of nodes in the linked list.
'''

class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        fast = head
        slow = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow
