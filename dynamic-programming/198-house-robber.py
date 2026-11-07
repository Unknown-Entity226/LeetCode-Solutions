"""
Problem Description:
Given an array nums where nums[i] represents the money available in the
ith house, find the maximum amount that can be robbed without robbing
two adjacent houses.

Approach:
Use recursive backtracking with memoization (top-down dynamic programming).

At every house, there are two choices:

1. Rob the current house:
   Add nums[index] to the maximum money obtainable from index + 2,
   since the next adjacent house cannot be robbed.

2. Skip the current house:
   Move to index + 1 and calculate the maximum money obtainable from
   the remaining houses.

Choose the maximum of these two possibilities and memoize the result
for the current index.

The recurrence relation is:

DP(index) = max(nums[index] + DP(index + 2), DP(index + 1))

Base case:
If index reaches or exceeds the array length, return 0.

Time Complexity: O(n)
Reason: Each index is evaluated only once due to memoization. Every
state performs constant work by evaluating two recursive choices.

Space Complexity: O(n)
Reason: The memoization dictionary stores at most n states, and the
recursive call stack can grow up to O(n).
"""

class Solution:
    def rob(self, nums: list[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        memo = {}

        def backtrack(index):

            if index>=len(nums):
                return 0

            if index in memo:
                return memo[index]

            memo[index] = max(nums[index] + backtrack(index+2), backtrack(index+1))

            return memo[index]

        money = backtrack(0)

        return money
