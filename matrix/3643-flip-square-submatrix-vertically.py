'''
Problem Description:
You are given an m x n matrix `grid`, and integers x, y, and k.

(x, y) represents the top-left corner of a k x k submatrix.
You need to flip this submatrix vertically, i.e.,
reverse the order of its rows while keeping columns intact.

Return the updated matrix.

Approach:
- The operation is equivalent to reversing rows within the submatrix.
- For each column from y to y + k - 1:
    - Use two pointers:
        - upper_row starting at x
        - lower_row starting at x + k - 1
    - Swap elements vertically until the pointers meet.
- Move column by column across the submatrix.

Time Complexity:
O(k^2), since we process a k x k submatrix.

Space Complexity:
O(1), in-place modification.
'''
class Solution(object):
    def reverseSubmatrix(self, grid, x, y, k):
        """
        :type grid: List[List[int]]
        :type x: int
        :type y: int
        :type k: int
        :rtype: List[List[int]]
        """
        upper_row = x
        lower_row = x + k - 1
        limit = k

        while limit:
            if upper_row >= lower_row:
                y += 1
                limit -= 1
                upper_row = x
                lower_row = x + k - 1
            else:
                temp = grid[upper_row][y]
                grid[upper_row][y] = grid[lower_row][y]
                grid[lower_row][y] = temp
                upper_row += 1
                lower_row -= 1

        return grid
