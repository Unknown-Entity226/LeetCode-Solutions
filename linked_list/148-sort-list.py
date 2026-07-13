"""
Problem Description:
Given the head of a singly linked list, sort the list
in ascending order and return the sorted head.

Approach:
- Use Merge Sort on the linked list.
- Find the middle node using the slow and fast pointer technique.
- Split the list into two halves.
- Recursively sort both halves.
- Merge the two sorted linked lists.
- Return the head of the merged list.

Time Complexity:
O(n log n)

Reason:
- Finding the middle takes O(n).
- Merging two sorted lists takes O(n).
- The list is divided into halves for log n levels.
- Total work across all levels is O(n log n).

Space Complexity:
O(log n)

Reason:
- Recursive Merge Sort creates a recursion stack of depth log n.
- The merge operation reuses existing nodes and does not create
  additional lists.
- Excluding the recursion stack.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def findMid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def merge(self, left, right):

        if not left:
            return right
        if not right:
            return left

        dummy = ListNode(0)
        curr =  dummy

        while left and right:
            if left.val<right.val:
                curr.next = left
                left = left.next
                curr = curr.next
            else:
                curr.next = right
                right = right.next
                curr = curr.next

        while left:
            curr.next = left
            left = left.next
            curr = curr.next

        while right:
            curr.next = right
            right = right.next
            curr = curr.next

        return dummy.next
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        mid = self.findMid(head)

        left = head
        right = mid.next
        mid.next = None

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left, right)
