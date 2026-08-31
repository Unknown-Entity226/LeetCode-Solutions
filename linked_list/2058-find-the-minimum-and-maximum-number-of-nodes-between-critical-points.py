"""
Problem Description:
Given a linked list, identify all critical points, where a
node is either a local maximum or a local minimum.

Return:
- The minimum distance between any two critical points.
- The maximum distance between any two critical points.

If fewer than two critical points exist, return [-1, -1].

Approach:
- Traverse the linked list using previous and current nodes.
- Track the 1-based index of each node.
- A node is a critical point if its value is strictly
  greater than both neighbors or strictly smaller than both.
- Store the indices of all critical points.
- If fewer than two critical points exist, return [-1, -1].
- The maximum distance is the distance between the first
  and last critical points.
- The minimum distance is the minimum difference between
  consecutive critical point indices.

Time Complexity:
O(n)

Reason:
- The linked list is traversed once.
- Finding the minimum distance among critical points takes
  O(c), where c <= n.
- Therefore, total complexity is O(n).

Space Complexity:
O(c)

Reason:
- The critical list stores the indices of all critical
  points.
- In the worst case, O(n) critical points can exist.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        critical = []

        result = [-1, -1]
        if not head or not head.next :
            return result
        prev = head
        curr = head.next
        idx = 2
        while curr.next:
            if (curr.val>prev.val and curr.val>curr.next.val) or (curr.val<prev.val and curr.val< curr.next.val):

                critical.append(idx)
            idx+=1
            curr = curr.next
            prev = prev.next
        
        if len(critical)<2:
            return result

        maxDis = critical[-1]-critical[0]

        minDis = maxDis

        for i in range(1, len(critical)):
            minDis = min(minDis, critical[i]-critical[i-1])

        return [minDis, maxDis]

                
