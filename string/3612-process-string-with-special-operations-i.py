"""
Problem Description:
Given a string s containing:
- lowercase letters
- '*'
- '#'
- '%'

Build a string result using these rules:

    letter -> append to result
    '*'    -> remove the last character if it exists
    '#'    -> duplicate the current result
    '%'    -> reverse the current result

Return the final result.

Approach:
- Maintain a string ans.
- Process characters from left to right.
- Apply the corresponding operation for each character:
    - append
    - delete last character
    - duplicate string
    - reverse string

Time Complexity:
O(n + total output size)

Space Complexity:
O(final result size)
"""

class Solution(object):

    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """

        ans = ""

        for i in s:

            if i == "*":

                if ans:
                    ans = ans[:-1]

            elif i == "#":

                ans += ans

            elif i == "%":

                ans = ans[::-1]

            else:

                ans += i

        return ans
