"""
Problem Description:
Given a string s and an integer k, reverse the first k characters
for every 2k characters starting from the beginning of the string.

Rules:
- If fewer than k characters remain, reverse all of them.
- If at least k but fewer than 2k characters remain, reverse only
  the first k characters and leave the rest unchanged.

Approach:
- Convert the string into a list so that characters can be modified in-place.
- Iterate through the string in steps of 2k.
- For every block, use two pointers:
    - left starts at the beginning of the block.
    - right starts at the end of the first k characters.
- Limit right using min() so that the pointer never goes beyond
  the end of the string.
- Swap characters while left < right to reverse the required section.
- Convert the character list back into a string.

Time Complexity:
O(n)

Reason:
- Every character participates in at most one reversal.
- The outer loop skips by 2k, while the total number of swaps
  across all blocks is O(n).

Space Complexity:
O(n)

Reason:
- The string is converted into a character list of size n.
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        arr = list(s)

        for i in range(0, len(arr), 2 * k):
            left = i
            right = min(i + k - 1, len(arr) - 1)

            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        return "".join(arr)
