"""
Problem Description:
Given two integer arrays target and arr of equal length,
determine whether arr can be transformed into target by
reversing any number of non-empty subarrays.

Approach:
Observe that reversing a subarray only changes the order
of elements—it never changes their values or frequencies.

Since any permutation of an array can be obtained through
a sequence of subarray reversals, the two arrays can be
made equal if and only if they contain exactly the same
elements with the same frequencies.

- Sort both arrays.
- Compare corresponding elements.
- If every element matches, return True.
- Otherwise, return False.

Time Complexity:
O(n log n)

Space Complexity:
O(1)
- Ignoring the space used by the sorting algorithm.
"""

class Solution(object):

    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """

        target.sort()
        arr.sort()

        for i in range(len(target)):

            if target[i] != arr[i]:
                return False

        return True
