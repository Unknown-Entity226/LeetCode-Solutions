"""
Problem Description:
Given a string s consisting only of 'a', 'b', and 'c',
return the number of substrings that contain at least
one occurrence of all three characters.

Approach:
Use a sliding window.

- Expand the window by moving the right pointer.
- Maintain the frequency of 'a', 'b', and 'c' in the window.
- Whenever the window contains all three characters:
    - Every substring starting at left and ending at
      right or beyond is valid.
    - Add:

          len(s) - right

      to the answer.
    - Shrink the window from the left to find more valid
      starting positions.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

class Solution(object):

    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        freq = {
            'a': 0,
            'b': 0,
            'c': 0
        }

        left = 0
        count = 0

        for right in range(len(s)):

            freq[s[right]] += 1

            while freq['a'] > 0 and freq['b'] > 0 and freq['c'] > 0:

                count += len(s) - right

                freq[s[left]] -= 1
                left += 1

        return count
