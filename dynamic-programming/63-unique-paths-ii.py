"""
Problem Description:
Given an m x n grid containing obstacles (1) and empty cells (0), find
the number of unique paths from the top-left corner to the bottom-right
corner. The robot can only move right or down and cannot enter obstacles.

Approach:
Use recursive backtracking with memoization (top-down dynamic programming).

For each cell (x, y):
1. If the cell is outside the grid, return 0.
2. If the cell contains an obstacle, return 0.
3. If the cell is the destination, return 1.
4. Otherwise, calculate the sum of paths from the cell below and the
   cell to the right.

Memoize the result for each valid cell to avoid recalculating subproblems.

Time Complexity: O(m * n)
Reason: Each cell is evaluated at most once, and each evaluation performs
constant work apart from two recursive calls.

Space Complexity: O(m * n)
Reason: The memoization dictionary stores at most m * n states. The
recursive call stack requires at most O(m + n) space.
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        
        memo = {}
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        def backtrack(x, y):
            if x>=m or y>=n:
                return 0

            if obstacleGrid[x][y] ==1 :
                return 0
                
            if (x, y) == (m-1, n-1):
                return 1

            if (x, y) in memo:
                return memo[(x, y)]


            memo[(x, y)] = backtrack(x+1, y) + backtrack(x, y+1)

            return memo[(x, y)]

        count = backtrack(0, 0)

        return count
