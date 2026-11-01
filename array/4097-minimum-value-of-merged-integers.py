"""
Problem Description:
Given an even-length integer array, merge consecutive elements into pairs
by concatenating their decimal representations. Return the minimum merged
integer among all pairs.

Approach:
Iterate through the array using a step size of 2.

For each pair:
1. Convert both integers into strings.
2. Concatenate the strings in the given order.
3. Convert the concatenated string back into an integer.
4. Update the minimum merged value.

Return the minimum value after processing all pairs.

Time Complexity: O(n * d)
Reason: We process n/2 pairs. Each pair requires string concatenation and
integer conversion, taking O(d) time, where d is the maximum number of
digits in an element.

Space Complexity: O(d)
Reason: Temporary strings are created for each pair, requiring space
proportional to the number of digits in the pair.
"""
class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:

        m = float("inf")

        for i in range(0, len(nums)-1, 2):

            m = min(m, int(str(nums[i])+str(nums[i+1])))

        return m
