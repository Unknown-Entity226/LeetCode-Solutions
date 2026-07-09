"""
Problem Description:
Given an array where every number appears either once or
twice, return the bitwise XOR of all numbers that appear
exactly twice.

If no number appears twice, return 0.

Approach:
- Use a hashmap to count the frequency of each number.
- Traverse the frequency map.
- XOR every number whose frequency is 2.
- Return the accumulated XOR.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""

class Solution(object):

    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        storage = {}

        for i in nums:

            if i in storage:
                storage[i] += 1

            else:
                storage[i] = 1

        ans = 0

        for i in storage:

            if storage[i] > 1:

                if ans == 0:
                    ans = i

                else:
                    ans = ans ^ i

        return ans
