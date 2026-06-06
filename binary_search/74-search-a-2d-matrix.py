"""
Problem Description:
Given an m × n matrix where:
- Each row is sorted.
- The first element of a row is greater than the last
  element of the previous row.

Return True if target exists in the matrix, otherwise False.

Approach:
- Use binary search on the rows to locate the only row
  that could contain the target.
- Once the candidate row is found, perform binary search
  within that row.

Time Complexity:
O(log m + log n)

Space Complexity:
O(1)
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rowUp = 0
        rowDown = len(matrix) - 1

        left = 0
        right = len(matrix[0]) - 1

        while rowUp <= rowDown:

            midRow = (rowUp + rowDown) // 2

            if matrix[midRow][len(matrix[0]) - 1] < target:
                rowUp = midRow + 1

            else:

                if matrix[midRow][0] <= target:

                    while left <= right:

                        mid = (left + right) // 2

                        if target == matrix[midRow][mid]:
                            return True

                        elif target < matrix[midRow][mid]:
                            right = mid - 1

                        else:
                            left = mid + 1

                    else:
                        break

                else:
                    rowDown = midRow - 1

        return False
