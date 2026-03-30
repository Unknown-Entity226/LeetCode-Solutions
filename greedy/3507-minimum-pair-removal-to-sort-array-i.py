'''
Problem Description:
You are given an array nums.

You can repeatedly perform the following operation:
- Select the adjacent pair with the minimum sum (if multiple, choose the leftmost).
- Replace the pair with their sum.

Return the minimum number of operations needed to make the array non-decreasing
(i.e., nums[i] <= nums[i+1] for all valid i).

Approach:
- Define a helper function to check if the array is non-decreasing.
- While the array is not non-decreasing:
    1. Find the adjacent pair with the minimum sum (leftmost if ties).
    2. Replace the pair with their sum:
          nums[index] = nums[index] + nums[index + 1]
          remove nums[index + 1]
    3. Increment the operation count.
- Continue until the array becomes non-decreasing or has size <= 1.

Greedy Rationale:
- Always merging the pair with the smallest sum minimizes local disruption
  and follows the problem’s rule for choosing the pair.

Time Complexity:
O(n^2) in the worst case. 

Space Complexity:
O(1) extra space (in-place modification).
'''
class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def isSorted(array):
            for i in range(len(array) - 1):
                if array[i] > array[i + 1]:
                    return False
            return True

        operations = 0

        while not isSorted(nums) and len(nums) > 1:
            small = nums[0] + nums[1]
            index = 0

            for i in range(len(nums) - 1):
                if nums[i] + nums[i + 1] < small:
                    small = nums[i] + nums[i + 1]
                    index = i

            nums[index] = small
            nums.pop(index + 1)
            operations += 1

        return operations
