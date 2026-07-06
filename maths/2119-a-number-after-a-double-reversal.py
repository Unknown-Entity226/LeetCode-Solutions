"""
Problem Description:
Given an integer num:

1. Reverse its digits.
2. Reverse the result again.

Return True if the final value equals the original
number, otherwise return False.

Approach:
Observe that:

- Reversing an integer removes all leading zeros.
- Therefore, if the original number ends with one or
  more zeros, those zeros are lost after the first
  reversal and cannot be recovered.
- The only exception is 0 itself.

Hence:
- If num == 0, return True.
- If num ends with 0, return False.
- Otherwise, return True.

Time Complexity:
O(1)

Space Complexity:
O(1)
"""

class Solution(object):

    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num == 0:
            return True

        if num % 10 == 0:
            return False

        return True21
