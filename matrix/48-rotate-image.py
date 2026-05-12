'''
Problem Description:
Given an n x n 2D matrix representing an image,
rotate the image by 90 degrees clockwise.

The rotation must be done IN-PLACE,
meaning no additional 2D matrix may be allocated.

Approach:
The rotation can be achieved in two steps:

1. Transpose the matrix
   - Swap matrix[i][j] with matrix[j][i]
   - Converts rows into columns

2. Reverse each row
   - This completes the clockwise 90-degree rotation

Example:

Original:
[1,2,3]
[4,5,6]
[7,8,9]

After transpose:
[1,4,7]
[2,5,8]
[3,6,9]

After row reversal:
[7,4,1]
[8,5,2]
[9,6,3]

Time Complexity:
O(n^2)

Space Complexity:
O(1), in-place modification.
'''
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        curr_row =0
        i = 0
        while curr_row<n:
            matrix[i][curr_row], matrix[curr_row][i] = matrix[curr_row][i], matrix[i][curr_row]
            if i == n-1:
                curr_row+=1
                i= curr_row
            else:
                i+=1
        i = 0
        curr_row = 0
        while i<n//2:
            matrix[curr_row][i], matrix[curr_row][n-i-1] = matrix[curr_row][n-i-1], matrix[curr_row][i]
            if curr_row == n-1:

                i+=1
                curr_row = 0
            else:
                curr_row+=1
