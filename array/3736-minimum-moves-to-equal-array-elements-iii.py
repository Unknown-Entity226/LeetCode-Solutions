"""
Problem Description:
Given an integer array nums, find the minimum number of moves required
to make all elements equal. In one move, any single element can be
increased by 1.

Approach:
Find the maximum element in the array.

Since elements can only be increased, the optimal target value is the
maximum element. Increasing the target beyond the maximum would only
require additional moves.

Iterate through the array and calculate the difference between the
maximum element and each element.

Sum these differences to obtain the minimum total number of moves.

Time Complexity: O(n)
Reason: Finding the maximum takes O(n), and calculating the total
difference requires another O(n) traversal.

Space Complexity: O(1)
Reason: Only a constant number of variables are used, regardless of
the input array size.
"""

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        m = max(nums)

        moves = 0

        for i in nums:
            moves+= m-i


        return moves
