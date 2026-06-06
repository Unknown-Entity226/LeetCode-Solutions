"""
Problem Description:
Given an array nums, define:

leftSum[i]:
    Sum of all elements to the left of index i.

rightSum[i]:
    Sum of all elements to the right of index i.

Return an array answer where:

    answer[i] = |leftSum[i] - rightSum[i]|

Approach:
- Compute the total sum of the array.
- Maintain a running leftSum.
- For each index:
    - Remove nums[i] from total.
      Now total represents rightSum.
    - Compute:
          abs(leftSum - rightSum)
    - Add nums[i] to leftSum for future indices.
- Store the result in the answer array.

Time Complexity:
O(n)

Space Complexity:
O(n)
- For output array.
"""

class Solution(object):

    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        answer = [0] * len(nums)

        total = sum(nums)
        leftSum = 0

        for i in range(len(nums)):

            total -= nums[i]

            answer[i] = abs(leftSum - total)

            leftSum += nums[i]

        return answer
