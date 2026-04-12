'''
Problem Description:
Given an integer rowIndex (0-indexed), return the rowIndex-th row
of Pascal's Triangle.

In Pascal's Triangle:
- First and last elements are always 1.
- Each inner element is the sum of the two elements directly above it.

Approach:
- Build Pascal's Triangle row by row up to rowIndex.
- Store all rows and return the last one.
- Each row is constructed using the previous row.

Time Complexity:
O(n^2), where n = rowIndex

Space Complexity:
O(n^2), since all rows are stored
'''
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        result = [[1], [1,1]]
        for i in range(2,rowIndex+1):
            temp= [1]
            for j in range(1, len(result[i-1])):
                temp.append(result[i-1][j-1]+result[i-1][j])
            temp.append(1)
            result.append(temp)
        return result[-1]
