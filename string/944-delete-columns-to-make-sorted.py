"""
Problem Description:
Given an array of equal-length strings, treat them as
rows of a grid.

Delete every column that is not sorted in
non-decreasing lexicographical order.

Return the number of such columns.

Approach:
- Traverse each column.
- For each column, compare every pair of adjacent rows.
- If any character is greater than the character directly
  below it, the column is unsorted.
- Count the column and move to the next one.

Time Complexity:
O(m × n)

Space Complexity:
O(1)
"""

class Solution(object):

    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """

        row, col = 0, 0

        count = 0

        for col in range(len(strs[0])):

            for row in range(len(strs) - 1):

                if strs[row][col] > strs[row + 1][col]:
                    count += 1
                    break

        return count
