'''
Problem Description:
Given an integer n, return True if it is a power of three.

An integer n is a power of three if there exists
an integer x such that:

    n = 3^x

Approach:
- The largest power of 3 that fits in a signed 32-bit integer is:

      3^19 = 1162261467

- If n is a power of 3,
  then n must divide 1162261467 exactly.

- Therefore:
      1162261467 % n == 0

- Also handle non-positive numbers separately.

Time Complexity:
O(1)

Space Complexity:
O(1)
'''
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n <= 0:
            return False

        return 1162261467 % n == 0
