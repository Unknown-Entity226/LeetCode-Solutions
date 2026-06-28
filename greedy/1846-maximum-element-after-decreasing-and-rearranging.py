"""
Problem Description:
Given an array of positive integers, you may:

1. Rearrange the elements in any order.
2. Decrease any element to a smaller positive integer.

After the operations, the array must satisfy:

- The first element is 1.
- The difference between adjacent elements is at most 1.

Return the maximum possible value in the final array.

Approach:
- Sort the array.
- Set the first element to 1.
- Traverse the remaining elements:
    - If the current element is more than 1 greater than
      the previous element, decrease it to:

          previous + 1

    - Otherwise, keep it unchanged.
- The last (or maximum) element obtained is the largest
  possible value satisfying the constraints.

Time Complexity:
O(n log n)

Space Complexity:
O(1)
- Ignoring the space used by the sorting algorithm.
"""

class Solution(object):

    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        arr.sort()

        arr[0] = 1

        maxElement = arr[0]

        for i in range(1, len(arr)):

            if (arr[i] - arr[i - 1]) > 1:
                arr[i] = arr[i - 1] + 1

            maxElement = max(maxElement, arr[i])

        return maxElement
