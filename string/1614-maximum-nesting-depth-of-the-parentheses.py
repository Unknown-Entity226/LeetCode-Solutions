"""
Problem Description:
Given a valid parentheses string, find its maximum nesting depth.
The nesting depth is the maximum number of parentheses that are open
at the same time.

Approach:
- Count the total number of opening and closing parentheses.
- Traverse the string from right to left.
- Maintain the number of unmatched opening parentheses using
  left - right.
- Update the maximum depth while processing the parentheses.

Time Complexity:
O(n)

Reason:
- The string is traversed twice.
- Both traversals take O(n), so the total remains O(n).

Space Complexity:
O(1)

Reason:
- Only a constant number of integer variables are used.
"""

class Solution:
    def maxDepth(self, s: str) -> int:
        left = 0
        right = 0

        for i in s:

            if i == "(":
                left+=1
            elif i ==")":
                right +=1
        

        depth = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == ")":
                right-=1
                depth = max(depth, left-right)

            elif s[i] == "(":
                left-=1
                depth = max(depth, left-right)

        return depth
