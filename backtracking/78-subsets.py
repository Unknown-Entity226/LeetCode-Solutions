"""
Problem Description:
Given an array of unique integers, return all possible
subsets (the power set).

The solution must not contain duplicate subsets.

Approach:
Use backtracking (include/exclude recursion).

For each element:
- Exclude it from the current subset.
- Include it in the current subset.
- Backtrack by removing the included element.

When all elements have been considered, store a copy
of the current subset.

Time Complexity:
O(n × 2^n)

Space Complexity:
O(n)
- Excluding the space required for the output.
"""
class Solution(object):

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        powerSet = []
        output = []
        idx = 0

        def subs(nums, idx, out, powerSet):

            if idx >= len(nums):
                powerSet.append(out[:])
                return

            # Exclude current element
            subs(nums, idx + 1, out, powerSet)

            # Include current element
            out.append(nums[idx])
            subs(nums, idx + 1, out, powerSet)

            # Backtrack
            out.pop()

        subs(nums, idx, output, powerSet)

        return powerSet
