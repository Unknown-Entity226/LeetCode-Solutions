"""
Problem Description:
Given the head of a linked list, swap every two adjacent
nodes and return the modified list.

- Node values cannot be modified.
- Only the links between nodes may be changed.

Approach:
Use recursion.

- Base Case:
    - If the list is empty or contains only one node,
      return it as is.
- Reverse the first two nodes using the standard
  iterative linked list reversal.
- Recursively swap the remaining list.
- Connect the tail of the swapped pair to the head
  returned by the recursive call.
- Return the new head of the swapped pair.

Time Complexity:
O(n)

Space Complexity:
O(n)
- Due to the recursive call stack.
"""

class Solution:

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Base case
        if not head or not head.next:
            return head

        # Reverse the first two nodes
        curr = head
        prev = None
        count = 0

        while curr and count < 2:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            count += 1

        # Recursively swap the remaining list
        head.next = self.swapPairs(temp)

        return prev
