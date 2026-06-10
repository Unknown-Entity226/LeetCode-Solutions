"""
Problem Description:
Given a positive integer n, return the number of 1's
in its binary representation.

This count is also known as the Hamming Weight.

Approach:
Use Brian Kernighan's Algorithm.

Observation:
- When we perform:

      n & (n - 1)

  the rightmost set bit (1-bit) of n is removed.

Example:

    n = 12

    1100
    1011
    ----
    1000

One set bit is removed.

Therefore:
- Repeatedly remove the rightmost set bit.
- Count how many times this operation can be performed
  before n becomes 0.

Time Complexity:
O(number of set bits)

Space Complexity:
O(1)
"""

class Solution(object):

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        count = 0

        while n:

            n = n & (n - 1)
            count += 1

        return count
