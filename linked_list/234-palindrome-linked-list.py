"""
Problem Description:
Given the head of a singly linked list, determine whether the linked
list is a palindrome.

Approach:
- Use slow and fast pointers to find the middle of the linked list.
- Store the first half of the list in a stack.
- If the list has an odd number of nodes, skip the middle node.
- Traverse the second half and compare each value with the top of the stack.
- The list is a palindrome if all values match.

Time Complexity:
O(n)

Reason:
- The slow/fast pointer traversal takes O(n).
- Comparing the second half with the stack takes O(n).
- Both operations together remain O(n).

Space Complexity:
O(n)

Reason:
- The stack stores approximately half of the linked list,
  resulting in O(n) auxiliary space.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        stack =[]
        if not head or not head.next:
            return True
        slow = head
        fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            stack.append(slow.val)
            slow = slow.next

        if fast:
            slow = slow.next
            # stack.pop()
        
        while  slow  and stack and stack[-1] == slow.val:
            stack.pop()
            slow = slow.next
        return True if not stack else False

        
