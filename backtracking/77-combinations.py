"""
Problem Description:
Given two integers n and k, return all possible
combinations of k numbers chosen from the range [1, n].

The combinations may be returned in any order.

Approach:
Use backtracking.

- Start choosing numbers from 1.
- At each recursive call:
    - Pick the current number.
    - Recursively choose the remaining numbers starting
      from the next integer.
    - Backtrack by removing the last chosen number.
- When k numbers have been selected, store a copy of the
  current combination.

Time Complexity:
O(k × C(n, k))

Space Complexity:
O(k)
- Excluding the space required for the output.
"""

class Solution(object):

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        output = []
        ans = []
        count = 0
        start = 1

        def recur(start, n, count, k, ans, output):

            if count >= k:
                output.append(ans[:])
                return

            for i in range(start, n + 1):

                ans.append(i)

                recur(i + 1, n, count + 1, k, ans, output)

                ans.pop()

        recur(start, n, count, k, ans, output)

        return output
