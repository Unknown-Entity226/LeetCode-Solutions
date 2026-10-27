"""
Problem Description:
Construct an m x n grid containing '.' and '#', such that exactly
one valid path exists from the top-left cell to the bottom-right cell.
Movement is allowed only to the right or downward.

Approach:
- Make the first row entirely free using n dots.
- Construct the remaining rows with n - 1 obstacles followed by
  one free cell.
- This leaves the first row as the only way to reach the last column
  from the starting cell, after which the last column provides the
  only route to the destination.

Time Complexity:
O(m * n)

Reason:
- Creating the first row takes O(n).
- Constructing the remaining m - 1 rows takes O(m * n) in total
  because each row contains n characters.
- Therefore, the overall time complexity is O(m * n).

Space Complexity:
O(m * n)

Reason:
- The grid stores m strings, each containing n characters.
- Therefore, the total space required for the grid is O(m * n).
"""
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:

        grid = []

        grid.append("."*n) #first row

        row = ("#"*(n-1))+"."
        for _ in range(1, m):
            grid.append(row)

        return grid
