"""
Problem Description:
Given an m x n grid containing non-negative integers, find the minimum
path sum from the top-left corner to the bottom-right corner. The robot
can only move right or down.

Approach:
Use recursive backtracking with memoization (top-down dynamic programming).

For each cell (x, y):
1. If the cell is outside the grid, return infinity because that path
   is invalid.
2. If the cell is the destination, return its value.
3. If the result for the current cell is already memoized, return it.
4. Otherwise, calculate the minimum cost of moving down or right and
   add the current cell's value.

The recurrence relation is:

DP(x, y) = grid[x][y] + min(DP(x + 1, y), DP(x, y + 1))

Memoization ensures that each cell's minimum remaining path sum is
calculated only once.

Time Complexity: O(m * n)
Reason: Each cell is evaluated at most once, and each evaluation performs
constant work apart from two recursive calls.

Space Complexity: O(m * n)
Reason: The memoization dictionary stores at most m * n states. The
recursive call stack requires at most O(m + n) space.
"""

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        

        memo = {}
        rows = len(grid)
        
        cols = len(grid[0])

        if (0,0) == (rows-1, cols-1):
            return grid[0][0]

        def backtrack(x, y):
            if x>=rows or y>=cols:
                return float("inf")

            if (x, y) == (rows-1, cols-1):
                return grid[x][y]

            if (x, y) in memo:
                return memo[(x,y)]

            memo[(x, y)] = grid[x][y] + min(backtrack(x+1, y),  backtrack(x, y+1))
            return memo[(x, y)]

        backtrack(0, 0)
        
        return memo[(0, 0)]

            
