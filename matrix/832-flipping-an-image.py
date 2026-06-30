"""
Problem Description:
Given a binary matrix:

1. Flip each row horizontally.
2. Invert every bit:
      0 -> 1
      1 -> 0

Return the resulting matrix.

Approach:
- Process each row independently.
- Use two pointers:
    - start from the left.
    - end from the right.
- Swap the elements while simultaneously inverting them.
- If both pointers meet at the middle element,
  invert it only once.

Time Complexity:
O(n²)

Space Complexity:
O(1)
"""

class Solution(object):

    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """

        size = len(image)

        for row in image:

            start = 0
            end = size - 1

            while start <= end:

                row[start], row[end] = row[end], row[start]

                if start == end:
                    row[start] = row[start] ^ 1

                else:
                    row[start] = row[start] ^ 1
                    row[end] = row[end] ^ 1

                start += 1
                end -= 1

        return image
