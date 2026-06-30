"""
Problem Description:
Given a 2D integer matrix, return its transpose.

The transpose of a matrix is obtained by swapping
rows and columns.

That is:

    transpose[row][col] = matrix[col][row]

Approach:
- Create a new matrix whose:
    - number of rows = original number of columns
    - number of columns = original number of rows
- Traverse every element of the original matrix.
- Place each element at its transposed position.

Time Complexity:
O(m × n)

Space Complexity:
O(m × n)
"""

class Solution(object):

    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        newMatrix = [[0] * len(matrix) for i in range(len(matrix[0]))]

        for row in range(len(matrix)):

            for col in range(len(matrix[0])):

                newMatrix[col][row] = matrix[row][col]

        return newMatrix
