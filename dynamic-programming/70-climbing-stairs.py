"""
Problem Description:
Given a staircase with target steps, determine the number of distinct
ways to reach the top when each move can climb either 1 or 2 steps.

Approach:
- Use recursion with memoization.
- Let recur(target) represent the number of ways to reach the top
  when target steps remain.
- From the current position, we can either:
    1. Climb 1 step -> recur(target - 1)
    2. Climb 2 steps -> recur(target - 2)
- Therefore:
      recur(target) = recur(target - 1) + recur(target - 2)
- Base cases:
    - target == 0: one valid way has been formed.
    - target == 1: one way.
    - target == 2: two ways.
- Store previously calculated results in memo to avoid repeated work.

Time Complexity:
O(n)

Reason:
- Each target value from 0 to n is calculated at most once due to
  memoization.

Space Complexity:
O(n)

Reason:
- The memo dictionary stores O(n) states.
- The recursion stack can also reach O(n).
"""

class Solution:
    def climbStairs(self, target: int) -> int:
        

        memo = {}

        def recur(target):
            if target==0:
                return 1
            if target ==1 or target==2:
                memo[target] = target
                return memo[target]
            if target<0:
                return 0
            
            if target in memo:
                return memo[target]

            memo[target] = recur(target-1)+recur(target-2)

            return memo[target]       

        return recur(target)

        
        
        
