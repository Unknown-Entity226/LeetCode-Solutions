"""
Problem Description:
Given a sorted integer array (possibly containing
negative numbers), return a new array containing the
squares of each number, also sorted in non-decreasing
order.

Approach:
Use two pointers.

- The largest square must come from either:
    - the leftmost element (largest negative), or
    - the rightmost element (largest positive).
- Compare the squares of both ends.
- Place the larger square at the end of the answer array.
- Move the corresponding pointer inward.
- Continue until all positions are filled.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""

class Solution(object):

    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        start = 0
        end = len(nums) - 1

        newArray = [0] * len(nums)

        idx = end

        while start <= end and idx >= 0:

            el1 = nums[start] * nums[start]
            el2 = nums[end] * nums[end]

            if el1 > el2:

                newArray[idx] = el1
                start += 1

            else:

                newArray[idx] = el2
                end -= 1

            idx -= 1

        return newArray
