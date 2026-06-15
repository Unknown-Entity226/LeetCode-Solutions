"""
Problem Description:
Given an integer num, repeatedly add its digits
until the result has only one digit.

Return that final single-digit number.

Approach:
Use the Digital Root property.

For any positive integer:

    digital_root = 1 + (num - 1) % 9

Equivalent form:

    if num == 0:
        return 0

    if num % 9 == 0:
        return 9

    return num % 9

This avoids repeatedly summing digits.

Time Complexity:
O(1)

Space Complexity:
O(1)
"""

class Solution(object):

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        if num == 0:
            return 0

        if num % 9 == 0:
            return 9

        return num % 9
