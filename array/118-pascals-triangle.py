'''
Problem Description:
Given an integer numRows, return the first numRows of Pascal's Triangle.

In Pascal's Triangle:
- The first and last element of each row is 1.
- Every other element is the sum of the two elements directly above it.

Approach:
- Handle base cases:
    - If numRows == 0 → return []
    - If numRows == 1 → return [[1]]
- Initialize the result with first two rows.
- For each subsequent row:
    - Start with [1]
    - For each middle element:
        value = prev_row[j-1] + prev_row[j]
    - End with 1
- Append each row to result.

Time Complexity:
O(n^2), since we generate all rows up to numRows.

Space Complexity:
O(n^2), for storing the triangle.
'''
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        result = [[1], [1,1]]
        for i in range(2,numRows):
            temp= [1]
            for j in range(1, len(result[i-1])):
                temp.append(result[i-1][j-1]+result[i-1][j])
            temp.append(1)
            result.append(temp)
        return result
