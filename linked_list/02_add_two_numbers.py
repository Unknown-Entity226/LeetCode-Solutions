'''
Problem Description:
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each node contains a single digit.
Add the two numbers and return the sum as a linked list.

The result should also be in reverse order.
The two numbers do not contain leading zeros except for the number 0 itself.

Approach:
- Use a result head node to simplify result list construction.
- Maintain a carry variable to handle sums >= 10.
- Traverse both linked lists simultaneously:
  - Add corresponding digits along with carry.
  - Create a new node with (total % 10).
  - Update carry as total // 10.
- Continue until both lists are exhausted AND carry becomes zero.
- Return result.next as the head of the result list.

Time Complexity:
O(max(n, m)), where:
  n = length of l1
  m = length of l2

Space Complexity:
O(max(n, m)), for the result linked list.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = ListNode()
        curr = result
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            total = carry

            if l1 is not None:
                total += l1.val
                l1 = l1.next

            if l2 is not None:
                total += l2.val
                l2 = l2.next

            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next

        return result.next
