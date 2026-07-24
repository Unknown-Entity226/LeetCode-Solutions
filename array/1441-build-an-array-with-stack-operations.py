"""
Problem Description:
Given a target array and a stream of integers from 1 to n,
return the sequence of "Push" and "Pop" operations needed
to construct the target array.

Approach:
- Traverse the stream from 1 onwards.
- Maintain a pointer to the current target element.
- For each number:
  - If it matches the current target element, perform
    "Push" and move to the next target element.
  - Otherwise, perform "Push" followed by "Pop" to
    discard it.
- Stop once all target elements have been constructed.

Time Complexity:
O(n)

Reason:
- Numbers from 1 up to the last target element are
  processed exactly once.
- Each number performs at most two operations.

Space Complexity:
O(1)

Reason:
- Excluding the output list.
- Only a few variables are used.
- The returned operations list is not counted as
  auxiliary space.
"""


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        operations = []
        idx = 0
        i = 1
        while i<=n and idx<len(target):

            if i == target[idx]:
                operations.append("Push")
                idx+=1
            else:

                operations.append("Push")
                operations.append("Pop")
            
            i+=1
        return operations
