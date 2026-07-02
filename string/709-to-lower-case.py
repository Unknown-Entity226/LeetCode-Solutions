"""
Problem Description:
Given a string s, replace every uppercase English letter
with its corresponding lowercase letter.

Return the resulting string.

Approach:
- Traverse the string character by character.
- If the character is an uppercase letter ('A' to 'Z'):
    - Convert it to lowercase using its ASCII value.
- Otherwise, keep it unchanged.
- Build and return the resulting string.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""

class Solution(object):

    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """

        ans = ""

        for i in s:

            if ord(i) >= 65 and ord(i) <= 90:
                ans += chr(97 + ord(i) - 65)

            else:
                ans += i

        return ans
