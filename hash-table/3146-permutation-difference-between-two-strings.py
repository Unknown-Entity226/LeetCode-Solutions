"""
Problem Description:
Given two strings s and t such that:

- Every character appears exactly once in s.
- t is a permutation of s.

The permutation difference is defined as the sum of the
absolute differences between the indices of each character
in s and its corresponding index in t.

Return the permutation difference.

Approach:
- Store the index of every character in s using a hashmap.
- Traverse t:
    - Look up the index of the current character in s.
    - Add the absolute difference between the two indices
      to the answer.
- Return the accumulated sum.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""

class Solution(object):

    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        mapping = {}

        for idx, value in enumerate(s):
            mapping[value] = idx

        total = 0

        for i in range(len(t)):
            total += abs(i - mapping[t[i]])

        return total
