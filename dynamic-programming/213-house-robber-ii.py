"""
Problem Description:
Given a circular array nums where nums[i] represents the money in the
ith house, find the maximum amount that can be robbed without robbing
two adjacent houses.

The first and last houses are also adjacent.

Approach:
Use recursive backtracking with memoization (top-down dynamic programming).

Since the houses are arranged in a circle, the first and last houses
cannot both be robbed.

Divide the problem into two independent cases:

1. Exclude the last house:
   Consider houses from index 0 to n-2.

2. Exclude the first house:
   Consider houses from index 1 to n-1.

For each case, use the standard House Robber recurrence:

DP(index) = max(
    nums[index] + DP(index + 2),
    DP(index + 1)
)

The first choice robs the current house and skips the next one.
The second choice skips the current house.

Use separate memoization dictionaries for both cases and return the
maximum result.

Time Complexity: O(n)
Reason: Each of the two cases processes at most n states. Every state
is evaluated once due to memoization.

Space Complexity: O(n)
Reason: The two memoization dictionaries collectively store O(n) states.
The recursive call stack can also grow up to O(n).
"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        
        if len(nums)==1:
            return nums[0]

        memo1= {}
        memo2= {}

        def backtrack(memo: dict, index: int, end: int):
            if index>=end:
                return 0

            if index in memo:
                return memo[index]

            memo[index] = max(nums[index]+backtrack(memo, index+2, end), backtrack(memo, index+1, end))
            return memo[index]

        money = max(backtrack(memo1, 0, len(nums)-1), backtrack(memo2,1, len(nums))) 

        return money           
