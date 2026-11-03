"""
Problem Description:
Given an integer array nums, find the minimum number of moves required
to make all elements equal. In one move, any element can be incremented
or decremented by 1.

Approach:
Use the mathematical property that the median minimizes the sum of
absolute differences between array elements and a common target.

1. Sort the array.
2. Select the median element as the target.
3. Calculate the absolute difference between every element and the median.
4. Sum these differences to obtain the minimum number of moves.

Time Complexity: O(n log n)
Reason: Sorting takes O(n log n), and calculating the total absolute
difference requires O(n) time.

Space Complexity: O(n)
Reason: Python's in-place sorting algorithm may require O(n) temporary
space in the worst case. Apart from sorting, the algorithm uses O(1)
auxiliary space.
"""

class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        
        nums.sort()

        median = nums[len(nums)//2]

        move = 0

        for i in nums:
            move+= abs(median - i)

        return move
