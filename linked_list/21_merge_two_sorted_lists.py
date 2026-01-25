'''Problem Description:
You are given the heads of two sorted singly linked lists, list1 and list2.
Merge the two lists into one sorted linked list.

The merged list should be created by splicing together nodes from the
original lists while maintaining sorted order.
Return the head of the merged linked list.

Approach:
- Create a dummy node (new_head) to simplify edge cases.
- Use a pointer (list3) to build the merged list starting from the dummy node.
- Traverse both lists simultaneously:
  - Compare the current values of list1 and list2.
  - Append the smaller value to the merged list.
  - Move forward in the list from which the value was taken.
- After one list is exhausted, append the remaining nodes of the other list.
- Return the node following the dummy head as the merged list head.

Time Complexity:
O(n + m), where:
  n = number of nodes in list1
  m = number of nodes in list2'''



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        new_head = ListNode()
        list3 = new_head

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                list3.next = ListNode(list1.val)
                list1 = list1.next
            else:
                list3.next = ListNode(list2.val)
                list2 = list2.next
            list3 = list3.next

        if list1 is not None:
            list3.next = list1
        else:
            list3.next = list2

        return new_head.next
