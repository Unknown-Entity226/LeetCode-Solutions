"""
Problem Description:
Given an array of distinct integers, return all possible
permutations.

The permutations can be returned in any order.

Approach:
Use backtracking with swapping.

- Fix one position at a time.
- For the current index:
    - Swap every remaining element into that position.
    - Recursively generate permutations for the rest of
      the array.
    - Swap back to restore the original state
      (backtracking).
- When all positions are fixed, store a copy of the
  current permutation.

Time Complexity:
O(n × n!)

Space Complexity:
O(n)
- Excluding the space required for the output.
"""

class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ans = []
        idx = 0

        def recur(nums, idx, ans):

            if idx >= len(nums) - 1:
                ans.append(nums[:])
                return

            for i in range(idx, len(nums)):

                nums[i], nums[idx] = nums[idx], nums[i]

                recur(nums, idx + 1, ans)

                nums[i], nums[idx] = nums[idx], nums[i]

        recur(nums, idx, ans)

        return ans
