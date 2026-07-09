"""
Problem Description:
A bit flip changes a single bit from:

    0 -> 1
or
    1 -> 0

Given two integers start and goal, return the minimum
number of bit flips required to convert start into goal.

Approach:
- XOR start and goal.
- In the XOR result:
    - A bit is 1 if the corresponding bits differ.
    - A bit is 0 if they are the same.
- Therefore, the answer is simply the number of set bits
  in the XOR result.

Time Complexity:
O(b)

Space Complexity:
O(1)

where b is the number of bits in the XOR result.
"""

class Solution(object):

    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """

        num = start ^ goal

        count = 0

        while num:

            digit = num % 2

            if digit == 1:
                count += 1

            num //= 2

        return count
