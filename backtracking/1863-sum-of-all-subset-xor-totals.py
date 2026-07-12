"""
Problem Description:
The XOR total of a subset is the XOR of all its elements.
The XOR total of the empty subset is 0.

Return the sum of the XOR totals of all possible subsets
of the given array.

Approach:
Use backtracking.

For each element:
- Exclude it from the current subset.
- Include it in the current subset by updating the
  running XOR.
- When all elements have been considered, add the
  current XOR value to the answer.

Time Complexity:
O(n × 2ⁿ)

Space Complexity:
O(n)
- Excluding the recursion output.
"""

class Solution(object):

    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = [0]
        idx = 0
        xor = 0

        def recur(nums, idx, ans, xor):

            if idx >= len(nums):
                ans[0] += xor
                return

            # Exclude current element
            recur(nums, idx + 1, ans, xor)

            # Include current element
            xor ^= nums[idx]
            recur(nums, idx + 1, ans, xor)

            # Backtrack
            xor ^= nums[idx]

        recur(nums, idx, ans, xor)

        return ans[0]
