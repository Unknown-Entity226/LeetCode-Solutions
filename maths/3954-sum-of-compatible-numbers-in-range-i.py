"""
Problem Description:
Given integers n and k, a positive integer x is called compatible if:

    abs(n - x) <= k
    (n & x) == 0

Return the sum of all compatible integers x.

Approach:
- Iterate through all possible values of x satisfying:

      n - k <= x <= n + k

- Since x must be positive:

      x >= 1

- For each candidate x:
    - Check if (n & x) == 0.
    - If true, add x to the answer.

Time Complexity:
O(k)

Space Complexity:
O(1)
"""

class Solution(object):

    def sumOfGoodIntegers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        total = 0

        for x in range(max(1, n - k), n + k + 1):

            if n & x == 0:
                total += x

        return total
