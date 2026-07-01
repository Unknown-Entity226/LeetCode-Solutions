"""
Problem Description:
Given two strings s and goal, determine whether goal can
be obtained by repeatedly moving the first character of s
to the end.

Approach:
- If the lengths are different, the answer is False.
- Concatenate s with itself.
- Every possible rotation of s appears as a substring of
  s + s.
- Therefore, check whether goal is a substring of s + s.

Time Complexity:
O(n)

Space Complexity:
O(n)
- Due to creating the string s + s.
"""

class Solution(object):

    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """

        if len(s) != len(goal):
            return False

        return goal in (s + s)
