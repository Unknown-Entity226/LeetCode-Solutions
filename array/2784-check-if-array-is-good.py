'''
Problem Description:
An array nums is considered good if it is a permutation of:

    base[n] = [1, 2, ..., n-1, n, n]

Meaning:
- Numbers from 1 to n-1 appear exactly once
- Number n appears exactly twice

Return True if nums is good, otherwise return False.

Approach:
- Find the maximum element m in nums.
- Sort the array.

- For a valid good array:
    nums should look like:
        [1, 2, 3, ..., m-1, m, m]

- Check:
    1. nums[i] == i+1 for all indices except last
    2. Last two elements are equal

- If all conditions hold → return True.

Time Complexity:
O(n log n), due to sorting.

Space Complexity:
O(1) extra space (ignoring sort overhead).
'''
class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) < 2:
            return False

        m = max(nums)

        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] != i + 1:
                return False

        if nums[-1] == nums[-2]:
            return True
        else:
            return False
