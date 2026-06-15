"""
Problem Description:
Given an integer num, return its representation
in base 7 as a string.
Approach:
- Store the sign separately.
- Work with the absolute value.
- Repeatedly:
    - Append num % 7 to the result.
    - Divide num by 7.
- Append the final digit.
- Add '-' if the original number was negative.
- Reverse the constructed string because digits are
  obtained from least significant to most significant.

Time Complexity:
O(log₇ n)

Space Complexity:
O(log₇ n)
- For the output string.
"""

class Solution(object):

    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """

        result = ""

        sign = 1 if num < 0 else 0

        num = abs(num)

        while num >= 7:

            result += str(num % 7)
            num //= 7

        result += str(num)

        if sign:
            result += "-"

        return result[::-1]
