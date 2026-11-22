"""
Problem Description:
Given a string s containing only 'a' and 'b', determine whether every
occurrence of 'a' appears before every occurrence of 'b'.

Approach:
Use two traversals to identify the boundary between the two characters.

1. Traverse from left to right to find the first occurrence of 'b'.
   If no 'b' exists, keep its position as len(s).
2. Traverse from right to left to find the last occurrence of 'a'.
   If no 'a' exists, keep its position as 0.
3. Compare the two positions:
   - If the first 'b' occurs after the last 'a', the string is valid.
   - Otherwise, an 'a' appears after a 'b', so return False.

Time Complexity: O(n)
Reason: Two traversals are performed, each taking at most O(n) time.

Space Complexity: O(1)
Reason: Only two position variables and loop variables are used.
"""

class Solution:
    def checkString(self, s: str) -> bool:
        
        # first b
        b_pos = len(s)

        for i in range(len(s)):

            if s[i] == "b":
                b_pos = i
                break

        # last a

        a_pos = 0

        for i in range(len(s)-1, -1, -1):

            if s[i] == "a":
                a_pos = i

                break

        return True if b_pos - a_pos >= 0 else False
        
