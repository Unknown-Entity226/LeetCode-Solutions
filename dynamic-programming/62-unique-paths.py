"""
Problem Description:
Given an m x n grid, find the number of unique paths from the top-left
corner to the bottom-right corner. The robot can only move right or down.

Approach:
Use recursive backtracking with memoization (top-down dynamic programming).

At each cell (x, y), recursively calculate:
1. Paths obtained by moving down: backtrack(x + 1, y)
2. Paths obtained by moving right: backtrack(x, y + 1)

The total paths from the current cell are the sum of these two results.

Base cases:
- If the robot reaches the destination, return 1.
- If the robot moves outside the grid, return 0.

Store the result for each visited cell in a memoization dictionary to avoid
recomputing the same subproblems.

Time Complexity: O(m * n)
Reason: Each valid cell is computed only once due to memoization.

Space Complexity: O(m * n)
Reason: The memoization dictionary stores at most m * n states, and the
recursive call stack can also grow up to O(m + n).
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        memo = {}    #(x, y) : count of paths from that position 

        def backtrack(x, y):

            if (x, y) == (m-1, n-1):
                return 1
            
            if x>=m or y>=n:
                return 0

            if (x, y) in memo:
                return memo[(x, y)]

            
            memo[(x, y)] = backtrack(x+1,y) + backtrack(x, y+1)

            return memo[(x,y)]

        count = backtrack(0, 0)

        return count

            
